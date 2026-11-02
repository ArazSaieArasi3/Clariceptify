"""Check the bounded Knowledge review without promoting full CQ execution."""
import json
from domain_review_checks import check

if __name__ == "__main__":
    print(json.dumps(check("knowledge", 108, 17, 1), indent=2))
