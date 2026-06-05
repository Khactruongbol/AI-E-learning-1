import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from einstein_csp import (  # noqa: E402
    backtracking_search,
    build_problem,
    immediate_right,
    next_to,
    ac3,
)


class EinsteinCSPTest(unittest.TestCase):
    def test_immediate_right_constraint(self):
        self.assertTrue(immediate_right(3, 2))
        self.assertTrue(immediate_right(5, 4))
        self.assertFalse(immediate_right(2, 3))
        self.assertFalse(immediate_right(4, 2))

    def test_next_to_constraint(self):
        self.assertTrue(next_to(1, 2))
        self.assertTrue(next_to(4, 5))
        self.assertFalse(next_to(1, 3))
        self.assertFalse(next_to(3, 3))

    def test_all_different_constraint_rejects_duplicate_group_values(self):
        csp = build_problem()

        self.assertFalse(csp.is_consistent({"Red": 1, "Green": 1}))
        self.assertFalse(csp.is_consistent({"Brit": 2, "Japanese": 2}))
        self.assertTrue(csp.is_consistent({"Red": 1, "Green": 2}))

    def test_ac3_keeps_domains_non_empty(self):
        csp = build_problem()

        self.assertTrue(ac3(csp))
        self.assertTrue(all(csp.domains[variable] for variable in csp.variables))

    def test_backtracking_finds_complete_solution(self):
        csp = build_problem()

        solution = backtracking_search(csp)

        self.assertIsNotNone(solution)
        self.assertEqual(25, len(solution))

    def test_final_answer(self):
        csp = build_problem()

        solution = backtracking_search(csp)

        self.assertEqual(solution["Japanese"], solution["Zebra"])
        self.assertEqual(solution["Norwegian"], solution["Water"])


if __name__ == "__main__":
    unittest.main()
