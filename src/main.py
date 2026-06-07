"""Main runner for the group source code."""

from __future__ import annotations

from einstein_csp import ac3, backtracking_search, build_problem, format_solution


def main() -> None:
    problem = build_problem()

    if not ac3(problem):
        raise SystemExit("AC-3 found an inconsistent problem.")

    solution = backtracking_search(problem)
    if solution is None:
        raise SystemExit("No solution found.")

    print(format_solution(solution))


if __name__ == "__main__":
    main()
