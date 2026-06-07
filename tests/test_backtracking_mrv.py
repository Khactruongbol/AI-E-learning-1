import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from backtracking_mrv import solve  # noqa: E402


class BacktrackingMRVTest(unittest.TestCase):
    def test_solution(self):
        zebra_owner, water_drinker = solve()

        self.assertEqual("Japanese", zebra_owner)
        self.assertEqual("Norwegian", water_drinker)


if __name__ == "__main__":
    unittest.main()
