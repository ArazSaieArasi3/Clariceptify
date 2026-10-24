# Repository instructions

## Language

All repository-facing content must be written in English. This includes issue titles and bodies, acceptance and non-acceptance criteria, comments, pull requests, reviews, commit messages, filenames, documentation, diagrams, generated artifacts, release notes, Wiki and Pages. Do not write Persian text or Persian/Arabic-script digits in these surfaces. Conversation language does not change this rule.

Preserve stable identifiers, issue numbers, links, dependencies, evidence qualifications and task states when translating existing material. Translate prose faithfully rather than deleting requirements. Use English renderings and external provenance pointers for non-English source material; do not copy that material into public artifacts.

Run `python tools/check_repository_language.py` before proposing changes. This checks local file paths and UTF-8 text, not remote discussions; independently check issue, comment, PR and release text before posting. The file check is a script-block guard, not proof that every sentence is English.

## Scientific and release boundaries

Follow the authority, identifiers, versioning and release decisions under `docs/decisions/`. Preserve unassessed, pending and candidate states unless actual new evidence supports a transition. Do not infer semantic adequacy, human approval, DOI issuance or publication from structural checks. Do not overwrite a published tag or asset. Do not modify upstream repositories as part of local migration work.

Keep tasks bounded, with concrete deliverables, AC/NAC and input-bound evidence. Close an issue only when its actual criteria are met. Generated representations are not independent semantic authorities.
