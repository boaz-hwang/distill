"""Check the four distributable skills after copying them out of the repository."""

import re
import shutil
import tempfile
import unittest
from pathlib import Path

from skills_ref import validate

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {"distill", "refine", "evolve", "consolidate"}


class SkillPackageTests(unittest.TestCase):
    def test_expected_skills_are_present(self):
        found = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
        self.assertEqual(found, SKILLS)

    def test_standalone_installations(self):
        with tempfile.TemporaryDirectory() as directory:
            for name in sorted(SKILLS):
                with self.subTest(skill=name):
                    installed = Path(directory) / name
                    shutil.copytree(ROOT / "skills" / name, installed)
                    self.assertEqual(validate(installed), [])
                    self.assertEqual(
                        (installed / "LICENSE").read_text(), (ROOT / "LICENSE").read_text()
                    )
                    for document in installed.rglob("*.md"):
                        for link in re.findall(r"\]\(([^)]+)\)", document.read_text()):
                            if "://" in link or link.startswith("#"):
                                continue
                            target = (document.parent / link.split("#")[0]).resolve()
                            self.assertTrue(target.is_relative_to(installed.resolve()), link)
                            self.assertTrue(target.is_file(), f"{document.name}: {link}")


if __name__ == "__main__":
    unittest.main()
