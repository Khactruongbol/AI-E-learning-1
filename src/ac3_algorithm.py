"""AC-3 entry point for the Einstein CSP model.

The full AC-3 implementation lives in einstein_csp.py so the project keeps one
shared constraint model. This module is a small, named entry point for the AC-3
part of the group assignment.
"""

from __future__ import annotations

from einstein_csp import ac3, build_problem


def run_ac3():
    """Build the Einstein CSP and reduce its domains with AC-3."""

    problem = build_problem()
    ok = ac3(problem)
    return ok, problem.domains


if __name__ == "__main__":
    ac3_ok, domains = run_ac3()
    print("AC-3 result:", ac3_ok)
    for variable in sorted(domains):
        print(f"{variable:12}: {sorted(domains[variable])}")
