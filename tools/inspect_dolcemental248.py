"""Inspect a pinned native FOF file; publish symbols/locators, never raw source."""
from collections import Counter, defaultdict
from pathlib import Path
import argparse
import hashlib
import json
import re

SOURCE_SHA256 = '61a88f4d392b9659b53bee1329df17bc2640464e2f34c79c867a93a36d91e1dc'
SOURCE_COMMIT = '93734dbe35c931338b3b9aba66b75c250baf6655'
SOURCE_BLOB = '73047de266cd6c1ea684befd1d05b6294ecc5265'

# Source comments and short reviewer readings, not imported OWL definitions.
# The source line in the first field is a descriptive comment/section header.
TERMS = {
    'pt/1': (20, 'DOLCE fragment: particular; top-level category.', []),
    'per/1': (21, 'DOLCE fragment: perdurant.', []),
    'end/1': (22, 'DOLCE fragment: endurant.', []),
    'con/1': (23, 'DOLCE-CORE referenced concept; exact foundation edition unpinned.', []),
    'time/1': (24, 'Time interval.', []),
    'apo/1': (36, 'Agentive physical object constrained as an endurant.', ['end/1']),
    'napo/1': (37, 'Nonagentive physical object constrained as an endurant.', ['end/1']),
    'stative/1': (46, 'Perdurant-side stative in the source partition.', ['per/1']),
    'event/1': (49, 'Other branch of the perdurant partition; not imposed on sat.', ['per/1']),
    'state/1': (46, 'Stative branch to which mental states are assigned.', ['stative/1']),
    'process/1': (52, 'Stative branch disjoint from state in the file.', ['stative/1']),
    'presentAt/2': (56, 'Presence of a particular at a time interval.', []),
    'pc/3': (65, 'Participation of an endurant in a perdurant at a time.', []),
    'cf/3': (72, 'Concept classification of a particular at a time.', []),
    'ms/1': (95, 'Mental state constrained as a state with an agentive participant.', ['state/1']),
    'about1/3': (116, 'Mental state directed at a concept at a time; content unique across times.', []),
    'about2/3': (132, 'Reference to an entity through about1 and concept classification.', []),
    'intObj/2': (141, 'Entity in an intentional-object role at a time.', []),
    'intCont/2': (142, 'Concept in an intentional-content role at a time.', []),
    'belState/1': (154, 'Belief state constrained as state; not directly as ms.', ['state/1']),
    'desState/1': (154, 'Desire state constrained as state; not directly as ms.', ['state/1']),
    'needState/1': (154, 'Need state constrained as state; not directly as ms.', ['state/1']),
    'intState/1': (163, 'Intention-state typing is commented out; active disjointness/test references remain.', []),
    'bel/3': (184, 'Agent belief attitude defined via a belief state, about1 and participation.', []),
    'des/3': (184, 'Agent desire attitude defined via a desire state, about1 and participation.', []),
    'need0/3': (250, 'Mental need attitude projected through a need state.', []),
    'goal/3': (197, 'Selected desire or need0 subject to the source compatibility condition.', []),
    'sat/3': (207, 'Source condition is presence and classification; eventhood is not required.', []),
    'succ/2': (214, 'Temporal successor, typed, asymmetric, irreflexive and transitive.', []),
    'igoal/3': (229, 'Instrumental goal with a later goal and source-scoped satisfier implication.', []),
    'egoal/3': (239, 'Goal that is not an instrumental goal.', []),
    'need1/3': (251, 'Equivalent to instrumental goal in the source.', []),
    'need2/3': (252, 'Stronger instrumental condition with source-scoped satisfier biconditional.', []),
    'need3/3': (253, 'One-way necessary condition: end goal and mental need attitude.', []),
}
FOUNDATION = {'pt/1', 'per/1', 'end/1', 'con/1', 'time/1', 'apo/1', 'napo/1',
              'stative/1', 'event/1', 'state/1', 'process/1', 'presentAt/2', 'pc/3', 'cf/3'}
REFERENCED_ONLY = {'intState/1'}
COMMENT_STATES = {
    'pt/1': 'LABEL_ONLY', 'per/1': 'LABEL_ONLY', 'end/1': 'LABEL_ONLY',
    'con/1': 'LABEL_WITH_FOUNDATION_CITATION', 'time/1': 'LABEL_ONLY',
    'apo/1': 'LABEL_ONLY', 'napo/1': 'LABEL_ONLY',
    'stative/1': 'SECTION_HEADER_ONLY', 'event/1': 'NO_SYMBOL_SPECIFIC_COMMENT',
    'state/1': 'SECTION_HEADER_ONLY', 'process/1': 'NO_SYMBOL_SPECIFIC_COMMENT',
    'presentAt/2': 'DESCRIPTIVE_COMMENT', 'pc/3': 'SECTION_HEADER_ONLY',
    'cf/3': 'DESCRIPTIVE_COMMENT', 'ms/1': 'DESCRIPTIVE_COMMENT',
    'about1/3': 'DESCRIPTIVE_COMMENT', 'about2/3': 'LABEL_ONLY',
    'intObj/2': 'DESCRIPTIVE_COMMENT', 'intCont/2': 'DESCRIPTIVE_COMMENT',
    'belState/1': 'GROUP_HEADER_ONLY', 'desState/1': 'GROUP_HEADER_ONLY',
    'needState/1': 'GROUP_HEADER_ONLY', 'intState/1': 'COMMENTED_OUT_FORMULA_ONLY',
    'bel/3': 'GROUP_HEADER_ONLY', 'des/3': 'GROUP_HEADER_ONLY',
    'need0/3': 'DESCRIPTIVE_COMMENT', 'goal/3': 'DESCRIPTIVE_COMMENT',
    'sat/3': 'COMMENT_EVENT_INTENT_NOT_AXIOM_GUARD', 'succ/2': 'SECTION_HEADER_ONLY',
    'igoal/3': 'SECTION_HEADER_ONLY', 'egoal/3': 'SECTION_HEADER_ONLY',
    'need1/3': 'DESCRIPTIVE_COMMENT', 'need2/3': 'DESCRIPTIVE_COMMENT',
    'need3/3': 'DESCRIPTIVE_COMMENT',
}
BICONDITIONALS = {'pt/1': [28], 'per/1': [49], 'about2/3': [135],
                  'intObj/2': [147], 'intCont/2': [149], 'bel/3': [187],
                  'des/3': [188], 'need0/3': [190], 'goal/3': [202],
                  'sat/3': [211], 'igoal/3': [234], 'egoal/3': [242],
                  'need1/3': [261], 'need2/3': [267]}


def active_text(raw):
    # Retain offsets and line numbers while masking percent-comments.
    return '\n'.join(line[:line.index('%')] + ' ' * (len(line) - line.index('%'))
                     if '%' in line else line for line in raw.split('\n'))


def formulas(text):
    found = []
    for match in re.finditer(r'(?m)^[ \t]*fof\(([A-Za-z0-9_]+),[ \t]*(axiom|conjecture),', text):
        start = match.start(); depth = 0; end = None
        for i in range(text.index('(', start), len(text)):
            if text[i] == '(': depth += 1
            if text[i] == ')':
                depth -= 1
                if depth == 0:
                    end = i + 1; break
        if end is None or text[end:end + 1] != '.':
            raise ValueError(f'Unbalanced or unterminated FOF at {text.count(chr(10), 0, start) + 1}')
        found.append({'name': match.group(1), 'role': match.group(2),
                      'line': text.count('\n', 0, start) + 1,
                      'text': text[match.end():end - 1]})
    if not found or text.count('fof(') != len(found):
        raise ValueError('Unaccounted active FOF')
    return found


def predicates(formula):
    for match in re.finditer(r'\b([a-z][A-Za-z0-9_]*)\(', formula):
        i = match.end(); depth = 1; args = []
        while depth and i < len(formula):
            if formula[i] == '(': depth += 1
            elif formula[i] == ')': depth -= 1
            if depth: args.append(formula[i])
            i += 1
        if depth: raise ValueError('Unbalanced atomic predicate')
        yield f'{match.group(1)}/{0 if not args else 1 + "".join(args).count(",")}'


def inspect(path):
    data = path.read_bytes(); digest = hashlib.sha256(data).hexdigest()
    if digest != SOURCE_SHA256: raise ValueError('Selected upstream bytes changed')
    raw = data.decode('utf-8'); active = active_text(raw)
    forms = formulas(active)
    names = defaultdict(list); occurrences = defaultdict(lambda: {'axiom': set(), 'conjecture': set()})
    for row in forms:
        names[row['name']].append(row['line'])
        for symbol in set(predicates(row['text'])):
            occurrences[symbol][row['role']].add(row['line'])
    if set(occurrences) != set(TERMS) or set(TERMS) != set(COMMENT_STATES):
        raise ValueError(f'Unaccounted symbols: {set(occurrences) ^ set(TERMS)}')
    rows = []
    for symbol in sorted(TERMS):
        comment, gloss, parents = TERMS[symbol]
        rows.append({'symbol': symbol, 'origin': 'INLINED_DOLCE_FAMILY_EXCERPT' if symbol in FOUNDATION else 'LOCAL_NATIVE_SYMBOL',
                     'comment_or_header_line': comment, 'annotation_availability': COMMENT_STATES[symbol],
                     'reviewer_paraphrase': gloss, 'paraphrase_basis': 'SOURCE_FORMULAS_AND_AVAILABLE_COMMENTS',
                     'asserted_named_parents': parents,
                     'biconditional_formula_lines': BICONDITIONALS.get(symbol, []),
                     'active_axiom_lines': sorted(occurrences[symbol]['axiom']),
                     'conjecture_lines': sorted(occurrences[symbol]['conjecture']),
                     'definition_state': 'REFERENCED_ONLY_NO_ACTIVE_POSITIVE_TYPE' if symbol in REFERENCED_ONLY
                     else 'CONSTRAINED_OR_DEFINED_IN_ACTIVE_AXIOMS',
                     'source_iri': None, 'owl_deprecation': 'NOT_APPLICABLE_NATIVE_FOL'})
    return {'schema_version': '1.0', 'issue': 248, 'checked_on': '2026-10-30',
            'source_commit': SOURCE_COMMIT, 'source_blob_sha': SOURCE_BLOB, 'source_sha256': digest,
            'source_bytes': len(data), 'syntax': 'TPTP_FOF_STYLE',
            'direct_include_statements': len(re.findall(r'(?m)^[ \t]*include\(', active)),
            'formula_counts': dict(Counter(row['role'] for row in forms)),
            'duplicate_formula_names': {k: v for k, v in sorted(names.items()) if len(v) > 1},
            'active_predicates': len(rows), 'unary_predicates': sum(x['symbol'].endswith('/1') for x in rows),
            'binary_predicates': sum(x['symbol'].endswith('/2') for x in rows),
            'ternary_predicates': sum(x['symbol'].endswith('/3') for x in rows),
            'inlined_foundation_predicates': len(FOUNDATION), 'local_native_predicates': len(rows) - len(FOUNDATION),
            'referenced_only_local_predicates': sorted(REFERENCED_ONLY),
            'predicates': rows,
            'boundary': 'Static lexical census only. No full TPTP parser, prover, model finder, DOLCE import closure or proof reproduction.'}


def render_catalog(result):
    base = ('https://github.com/diporello/DOLCE-mental_states-needs/blob/'
            f'{SOURCE_COMMIT}/dolce_needs.p#L')
    lines = ['# DOLCE Mental: complete selected native-predicate glossary', '',
             'Issue #248. Selected exact author draft `dolce_needs.p`, SHA256 `' + SOURCE_SHA256 + '`.',
             'This is a FOL predicate/signature inventory: unary predicates are the closest native analogue of classes. '
             'There are no released OWL class IRIs, RDF definitions, deprecation flags or formal `include` directives in the selected file. '
             'Inlined DOLCE-family predicates and local symbols are counted separately; their edition and full imported closure remain unverified.', '',
             '| Symbol | Origin | Source annotation | Locator | Biconditional lines | Active axiom occurrences | Short source-bound reading |',
             '|---|---|---|---|---|---|---|']
    for row in result['predicates']:
        comment = row['comment_or_header_line']
        refs = ', '.join(f'[L{n}]({base}{n})' for n in row['active_axiom_lines'])
        bic = ', '.join(str(n) for n in row['biconditional_formula_lines']) or '—'
        lines.append(f"| `{row['symbol']}` | {row['origin']} | {row['annotation_availability']} | [L{comment}]({base}{comment}) | {bic} | {refs} | {row['reviewer_paraphrase']} |")
    lines += ['', 'The [machine-readable census](../../../evaluation/related-work/dolce-mental/technical-census.json) '
              'also gives every active conjecture locator, asserted named parent, reference-only status and four duplicate-name groups. '
              'The `intState/1` positive subtype line is commented; its active disjointness/test uses do not supply that definition. '
              'Comments are descriptive candidates, not sufficient formal definitions; source constraints at the listed lines control interpretation.', '',
              'Local source change: NONE. Clariceptify model change: NONE. Reasoner/prover result: NOT_EXECUTED.', '']
    return '\n'.join(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--markdown', type=Path)
    args = parser.parse_args()
    result = inspect(args.source)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    if args.markdown:
        args.markdown.write_text(render_catalog(result))
    print({k: result[k] for k in ('formula_counts', 'active_predicates', 'unary_predicates', 'binary_predicates', 'ternary_predicates', 'duplicate_formula_names')})
