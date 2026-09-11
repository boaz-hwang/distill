"""Exercise observable validator behavior using disposable skill packages."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from validate_skill import check


class ValidateSkillTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.skill = Path(self.temp.name) / "sample-skill"
        self.skill.mkdir()
        self.write_skill()

    def write_skill(self, name="sample-skill", description="Produce a report from a supplied dataset."):
        (self.skill / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: {description}\n---\n\nCreate the report.\n",
            encoding="utf-8",
        )

    def test_valid_skill_is_not_a_quality_claim(self):
        result = check(self.skill)
        self.assertTrue(result["passed"])
        self.assertEqual(result["outcome_quality"], "not_evaluated")
        self.assertEqual(result["python_files_checked"], [])

    def test_missing_skill_file(self):
        (self.skill / "SKILL.md").unlink()
        self.assertFalse(check(self.skill)["passed"])

    def test_wrong_directory_name(self):
        self.write_skill(name="another-name")
        self.assertFalse(check(self.skill)["passed"])

    def test_empty_description(self):
        self.write_skill(description='""')
        self.assertFalse(check(self.skill)["passed"])

    def test_malformed_yaml(self):
        (self.skill / "SKILL.md").write_text("---\nname: [\n---\n", encoding="utf-8")
        self.assertFalse(check(self.skill)["passed"])

    def test_invalid_metadata_type_fails_cleanly(self):
        self.write_skill(name="42")
        self.assertFalse(check(self.skill)["passed"])

    def test_missing_path(self):
        self.assertFalse(check(self.skill / "missing")["passed"])

    def test_broken_python_is_reported(self):
        scripts = self.skill / "scripts"
        scripts.mkdir()
        (scripts / "check.py").write_text("def broken(:\n", encoding="utf-8")
        result = check(self.skill)
        self.assertFalse(result["passed"])
        self.assertEqual(result["python_files_checked"], ["scripts/check.py"])

    def test_valid_python_is_never_executed(self):
        scripts = self.skill / "scripts"
        scripts.mkdir()
        marker = self.skill / "executed.txt"
        (scripts / "check.py").write_text(
            f"from pathlib import Path\nPath({str(marker)!r}).write_text('executed')\n",
            encoding="utf-8",
        )
        self.assertTrue(check(self.skill)["passed"])
        self.assertFalse(marker.exists())

    def test_invalid_python_context_is_reported(self):
        scripts = self.skill / "scripts"
        scripts.mkdir()
        (scripts / "check.py").write_text("return 1\n", encoding="utf-8")
        self.assertFalse(check(self.skill)["passed"])

    def test_cli_status_and_json(self):
        command = [sys.executable, str(ROOT / "tools/validate_skill.py"), str(self.skill)]
        good = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(good.returncode, 0, good.stderr)
        self.assertTrue(json.loads(good.stdout)["passed"])
        self.write_skill(name="wrong")
        bad = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1, bad.stderr)
        self.assertFalse(json.loads(bad.stdout)["passed"])


if __name__ == "__main__":
    unittest.main()
