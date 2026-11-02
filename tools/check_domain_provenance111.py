"""Check the bounded Provenance review without promoting full CQ execution."""
import json
from domain_review_checks import check

if __name__ == "__main__":
    print(json.dumps(check("provenance", 111, 20, 5), indent=2))
