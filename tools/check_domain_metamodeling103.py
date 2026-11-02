"""Check the bounded Metamodeling review without promoting full CQ execution."""
import json
from domain_review_checks import check

if __name__ == "__main__":
    print(json.dumps(check("metamodeling", 103, 12, 4), indent=2))
