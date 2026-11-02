"""Check the bounded Terminology review without promoting full CQ execution."""
import json
from domain_review_checks import check

if __name__ == "__main__":
    print(json.dumps(check("terminology", 102, 11, 10), indent=2))
