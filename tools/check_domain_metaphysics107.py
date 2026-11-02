"""Check the bounded Metaphysics review without promoting full CQ execution."""
import json
from domain_review_checks import check

if __name__ == "__main__":
    print(json.dumps(check("metaphysics", 107, 16, 3), indent=2))
