"""Check the bounded Evaluation review without promoting full CQ execution."""
import json
from domain_review_checks import check

if __name__ == "__main__":
    print(json.dumps(check("evaluation", 110, 19, 4), indent=2))
