"""Check the bounded Ontology review without promoting full CQ execution."""
import json
from domain_review_checks import check

if __name__ == "__main__":
    print(json.dumps(check("ontology", 106, 15, 1), indent=2))
