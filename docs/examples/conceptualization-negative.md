# Empty subject-union counterexample

Synthetic illustrative evidence, not an empirical study. Model: `input-r1-rev1`.

The [negative fixture](../../evaluation/fixtures/conceptualization-negative.yaml)
derives from the exact [positive episode](../../evaluation/fixtures/conceptualization-positive.yaml).
Removing CLR-R0043 through CLR-R0047 for the episode leaves each individual
optional branch empty, but violates the combined subject requirement in
[CLR-SC0001](../../model/constraints.yaml). The expected diagnostic is
`EMPTY_SUBJECT_UNION`, linked to FR-02 / CQ-02.

Run `python tools/check_conceptualization_fixtures.py --output /tmp/fixtures.json`.
The positive fixture is accepted for this one selected clause; the negative is
rejected for that diagnostic. The result does not execute other constraints,
prove global instance conformance, satisfy all CQs or constitute expert approval.
See the [actual result](../../evaluation/conceptualization-fixtures.json).
