"""Check the bounded Taxonomy review without promoting full CQ execution."""
import json
from domain_review_checks import check

if __name__ == "__main__":
    print(json.dumps(check("taxonomy", 104, 13, 3), indent=2))
