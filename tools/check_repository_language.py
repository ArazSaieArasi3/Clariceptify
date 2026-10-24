"""Reject Arabic/Persian script in current repository text and file paths.

This local guard does not inspect Git history, binary contents or remote metadata.
English prose still requires review; passing is not a general language classifier.
"""

from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = re.compile(r"[\u0600-\u06ff\u0750-\u077f\u0870-\u089f\u08a0-\u08ff\ufb50-\ufdff\ufe70-\ufeff\U00010e60-\U00010e7f\U00010ec0-\U00010eff\U0001ee00-\U0001eeff]")


def inspect(paths):
    findings = []
    text_files = 0
    binary_files = 0
    for name in sorted(set(paths)):
        if FORBIDDEN.search(name):
            findings.append({"path": name, "kind": "path"})
        path = ROOT / name
        if not path.is_file():
            continue
        data = path.read_bytes()
        try:
            if b"\x00" in data:
                raise UnicodeError("binary content")
            content = data.decode("utf-8")
        except UnicodeError:
            binary_files += 1
            continue
        text_files += 1
        for number, line in enumerate(content.splitlines(), 1):
            if FORBIDDEN.search(line):
                findings.append({"path": name, "line": number, "kind": "text"})
    return {"status": "FAIL" if findings else "PASS", "text_files": text_files,
            "binary_files_not_inspected": binary_files, "findings": findings,
            "scope": "current file paths and UTF-8 text; not discussions, history or binary contents"}


if __name__ == "__main__":
    paths = sys.argv[1:] or subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT).decode("utf-8").rstrip("\0").split("\0")
    result = inspect(paths)
    print(json.dumps(result, indent=2))
    raise SystemExit(result["status"] != "PASS")
