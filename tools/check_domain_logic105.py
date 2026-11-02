"""Check the bounded Logic review without promoting full CQ execution."""
import json
from domain_review_checks import check

if __name__ == "__main__":
    print(json.dumps(check("logic", 105, 14, 4), indent=2))
