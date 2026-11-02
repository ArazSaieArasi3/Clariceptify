"""Check the bounded Quality review without promoting full CQ execution."""
import json
from domain_review_checks import check

if __name__ == "__main__":
    print(json.dumps(check("quality", 109, 18, 5), indent=2))
