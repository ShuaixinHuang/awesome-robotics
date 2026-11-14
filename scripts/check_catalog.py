"""Offline checks for resource rows, navigation anchors and published counts."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ("robots", "embedded", "arch-os", "ml")


def check_catalog(text):
    errors = []
    counts = dict.fromkeys(SECTIONS, 0)
    names = set()
    anchors = re.findall(r'<a id="([^"]+)"></a>', text)
    if len(anchors) != len(set(anchors)):
        errors.append("Duplicate explicit navigation anchor")
    for target in re.findall(r"\]\(#([^)]+)\)", text):
        if target not in anchors:
            errors.append(f"Missing explicit navigation anchor: #{target}")
    section = None
    table_open = False
    for number, line in enumerate(text.splitlines(), 1):
        match = re.fullmatch(r'<a id="([^"]+)"></a>', line)
        if match and match[1] in counts:
            section = match[1]
        elif match and match[1] in ("top", "credits"):
            section = None
        if not line.strip():
            table_open = False
        if line.startswith("| 项目名称 |"):
            table_open = True
        if not line.startswith("| **"):
            continue
        if section not in counts:
            errors.append(f"Line {number}: resource outside a catalog section")
            continue
        counts[section] += 1
        if not table_open:
            errors.append(f"Line {number}: resource is detached from its table header")
        cells = [cell.strip() for cell in re.split(r"(?<!\\)\|", line)[1:-1]]
        if len(cells) != 4:
            errors.append(f"Line {number}: expected four resource columns")
            continue
        name = cells[0].strip("*").casefold()
        if name in names:
            errors.append(f"Line {number}: duplicate resource name {cells[0]}")
        names.add(name)
        if not re.search(r"\]\(https?://[^\s)]+\)", cells[2] or cells[3]):
            errors.append(f"Line {number}: expected a project or source link")
    summary = re.search(r"\*\*(\d+) 个资源条目\*\*", text)
    if summary is None or int(summary[1]) != sum(counts.values()):
        errors.append(f"Resource total must be {sum(counts.values())}")
    for section, total in counts.items():
        row = re.search(
            r"^\| \[.*?\]\(#" + re.escape(section) + r"\)\s*\|[^\n]*\|\s*(\d+)\s*\|$",
            text,
            re.M,
        )
        if row is None or int(row[1]) != total:
            errors.append(f"Navigation count for #{section} must be {total}")
    return counts, errors


def main():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    counts, errors = check_catalog(text)
    print(
        json.dumps(
            {"total": sum(counts.values()), "sections": counts, "errors": errors},
            ensure_ascii=False,
            indent=2,
        )
    )
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
