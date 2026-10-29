# I&DA: bounded technical discovery and paper-index inspection

Issue #246, checked 2026-10-30 against Clariceptify baseline `0663ebd00c10589666ed5c754cbd2d133bb27e47`. [Structured authority](IDA.yaml), [dated discovery receipt](../../../evaluation/related-work/ida/technical-discovery.json), and the separately completed [owner-summary review](../deep-reviews/CLR-RW-IDA/report.md) have distinct scopes.

The [author/workshop paper URL](https://www-sop.inria.fr/acacia/WORKSHOPS/ECAI2004-OM/articlesPDF/ecai2004-OM-Fortier-Kassel-13.pdf) yielded indexed excerpts from sections 3.1–4.1, but the checked direct open returned 502. Index extraction corrupts logical symbols. No original PDF bytes, executable I&DA file, authoritative formal version, class inventory or imports were acquired. Repository and code searches produced no identified author release within their checked scope; they cannot prove global absence. All machine populations, formal IRIs, foundation edition and source license are **unknown**, not zero. The 29 terms in the #84 summary are conceptual entries, not a released class glossary.

| Check | Printed-paper lead / prior summary | Evidence-bound result |
|---|---|---|
| T01: two sign layers | Indexed §3.1; SR004–005 | Sign/content and discourse/information overlap the model's information and representation area. No released IRI or class declaration is verified. |
| T02: grounding | Indexed §3.1, §3.2 n.9; SR007, SR013 | Paper names DOLCE as backbone and DOLCE-LITE+ for Action. Edition, actual formal import and validated alignment are unknown. |
| T03: sign and inscription | Indexed §3.2; SR015–017 | Text distinguishes content/sign from physical inscription and discusses `represents`/`realizes`. Glyph-corrupted formulas are not treated as executable axioms. |
| T04: acts | Indexed §3.2–3.3 n.6; SR013–014 | Conceptualizing, Encoding, Decoding and Inscribing are named; the thematic-role ontology is expressly omitted for space. |
| T05: production and transmission | Indexed §3.3; SR005, SR020–021 | Producer and transmitter, addressee and receiver are distinct roles; their identity cannot be silently asserted. |
| T06: truth | Indexed §4.1; SR022–023, SR026, SR037 | Organizational KB Assertions receive a local `True` attribution; varying discourse viewpoints remain possible. The summary's printed formula is not a certified transcription or general truth rule. |
| T07: subject | Indexed §4.1; SR025, SR027 | `hasForSubject` relates proposition to concept in printed prose, contrasting generic and individual subjects; executable property IRI and formal domain/range are unverified. |
| T08: responsibility and conflict | Indexed §3.3, §4.1; SR024, SR037 | Enunciating links authorship and addressed communication. A coherent, consensual KB does not erase conflicting textual viewpoints. No formal test ran. |

**Positive case:** Two documents report the same subject while their production, transmission, addressees and physical inscriptions differ. The paper offers useful distinctions for a future CQ about author and evidence provenance.

**Adverse case:** A messenger transmits a conflicting transcript. Identifying the messenger as its author or promoting the transcript to a `True` organizational KB assertion would lose both provenance and dissent. This is an analytical counterexample, not a reasoner result.

Carry this qualified overlap to #256 and #126. Candidate Clariceptify concepts include Agent, Concept, Conceptualization, Expression, Information Object and Representation; no `owl:equivalentClass`, accepted import or model change follows. The original module and complete local glossary are absent, so AC-2 and the repository/class supplement remain open; #246 stays **open**. A newly found original distribution must be pinned and inventoried before closure. The earlier owner waiver closes only #84's summary/citation task, without reinstating a PDF gate for that task.
