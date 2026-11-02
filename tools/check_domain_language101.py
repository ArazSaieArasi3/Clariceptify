"""Check the bounded Language review without promoting full CQ execution."""
import json
from domain_review_checks import check

if __name__ == "__main__":
    print(json.dumps(check("language", 101, 10, 12), indent=2))
