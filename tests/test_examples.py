import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_examples import validate  # noqa: E402


class ExampleValidationTest(unittest.TestCase):
    def test_all_examples_match_schemas(self):
        self.assertEqual(validate(), [])


if __name__ == "__main__":
    unittest.main()
