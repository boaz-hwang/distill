# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "skills-ref @ git+https://github.com/agentskills/agentskills.git@69ef37e9424c0a7ea9dd2293b559e43ec8176379#subdirectory=skills-ref",
# ]
# ///
"""Check Agent Skills format and bundled Python syntax, never execute target code."""

import argparse
import json
import sys
import tokenize
from pathlib import Path

from skills_ref import validate


def check(skill_dir: Path) -> dict:
    skill_dir = skill_dir.expanduser().absolute()
    errors = []
    checked = []
    try:
        errors.extend(validate(skill_dir))
    except (OSError, UnicodeError, ValueError, TypeError, AttributeError) as exc:
        errors.append(f"Cannot validate skill metadata: {exc}")

    # The standard requires this exact filename, even where a client is lenient.
    if skill_dir.is_dir() and not (skill_dir / "SKILL.md").is_file():
        errors.append("Missing required file: SKILL.md")

    scripts = skill_dir / "scripts"
    if scripts.is_dir():
        for script in sorted(scripts.rglob("*.py")):
            relative = str(script.relative_to(skill_dir))
            checked.append(relative)
            try:
                with tokenize.open(script) as source:
                    compile(source.read(), relative, "exec")
            except (OSError, UnicodeError, SyntaxError, ValueError) as exc:
                errors.append(f"{relative}: {exc}")

    return {
        "skill": str(skill_dir),
        "passed": not errors,
        "errors": list(dict.fromkeys(errors)),
        "python_files_checked": checked,
        "scope": "Agent Skills format and Python syntax only; no scripts executed.",
        "outcome_quality": "not_evaluated",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_dir", type=Path)
    result = check(parser.parse_args().skill_dir)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
