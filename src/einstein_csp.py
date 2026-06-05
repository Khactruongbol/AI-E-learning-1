"""Exercise 3.3 - Einstein's Riddle solved with CSP + AC-3 + Backtracking.

Main idea:
- Each attribute value is a variable: Red, Brit, Water, Zebra, ...
- The value of each variable is the house position: 1, 2, 3, 4, or 5.

Khac Truong's focus is marked in the code:
- All-Different constraints for each attribute group.
- Relative constraints: immediately right / next to.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Callable


HousePosition = int
Assignment = dict[str, HousePosition]
Predicate = Callable[[HousePosition, HousePosition], bool]

HOUSES = (1, 2, 3, 4, 5)

COLORS = ("Red", "Green", "Ivory", "Yellow", "Blue")
NATIONALITIES = ("Brit", "Spaniard", "Ukrainian", "Norwegian", "Japanese")
DRINKS = ("Coffee", "Tea", "Milk", "OrangeJuice", "Water")
TOBACCOS = ("OldGold", "Kools", "Chesterfields", "LuckyStrike", "Parliaments")
PETS = ("Dog", "Snails", "Fox", "Horse", "Zebra")

GROUPS = {
    "Color": COLORS,
    "Nationality": NATIONALITIES,
    "Drink": DRINKS,
    "Tobacco": TOBACCOS,
    "Pet": PETS,
}

DISPLAY_NAMES = {
    "OrangeJuice": "Orange Juice",
    "OldGold": "Old Gold",
    "LuckyStrike": "Lucky Strike",
}


@dataclass(frozen=True)
class Constraint:
    """One binary CSP constraint.

    AC-3 needs binary constraints, so All-Different is expanded into many
    pairwise constraints such as Red != Green, Red != Ivory, ...
    """

    left: str
    right: str
    predicate: Predicate
    note: str

    def check(self, assignment: Assignment) -> bool:
        """Return True for partial assignments until both variables are known."""

        if self.left not in assignment or self.right not in assignment:
            return True
        return self.predicate(assignment[self.left], assignment[self.right])

    def accepts(self, variable: str, value: int, other_value: int) -> bool:
        """Evaluate this constraint from either AC-3 arc direction."""

        if variable == self.left:
            return self.predicate(value, other_value)
        return self.predicate(other_value, value)


@dataclass
class CSP:
    variables: tuple[str, ...]
    domains: dict[str, set[HousePosition]]
    constraints: list[Constraint]

    def is_consistent(self, assignment: Assignment) -> bool:
        return all(constraint.check(assignment) for constraint in self.constraints)


def equal_position(left: HousePosition, right: HousePosition) -> bool:
    return left == right


def different(left: HousePosition, right: HousePosition) -> bool:
    return left != right


def immediate_right(right: HousePosition, left: HousePosition) -> bool:
    """True when the first variable is immediately right of the second."""

    return right == left + 1


def next_to(left: HousePosition, right: HousePosition) -> bool:
    return abs(left - right) == 1


def build_all_different_constraints() -> list[Constraint]:
    """Khac Truong task: no duplicate values inside each attribute group."""

    constraints: list[Constraint] = []
    for group_name, variables in GROUPS.items():
        for index, left in enumerate(variables):
            for right in variables[index + 1 :]:
                constraints.append(
                    Constraint(
                        left,
                        right,
                        different,
                        f"All-Different {group_name}: {left} != {right}",
                    )
                )
    return constraints


def build_relative_constraints() -> list[Constraint]:
    """Khac Truong task: model clues that depend on house positions."""

    return [
        Constraint(
            "Green",
            "Ivory",
            immediate_right,
            "Clue 5: Green is immediately right of Ivory",
        ),
        Constraint(
            "Chesterfields",
            "Fox",
            next_to,
            "Clue 10: Chesterfields is next to Fox",
        ),
        Constraint(
            "Kools",
            "Horse",
            next_to,
            "Clue 11: Kools is next to Horse",
        ),
        Constraint(
            "Norwegian",
            "Blue",
            next_to,
            "Clue 14: Norwegian is next to Blue",
        ),
        Constraint(
            "Chesterfields",
            "Water",
            next_to,
            "Clue 15: Chesterfields is next to Water",
        ),
    ]


def build_problem() -> CSP:
    variables = COLORS + NATIONALITIES + DRINKS + TOBACCOS + PETS
    domains = {variable: set(HOUSES) for variable in variables}

    # Unary clues are placed directly into domains to keep the code simple.
    domains["Milk"] = {3}
    domains["Norwegian"] = {1}

    constraints = [
        Constraint("Brit", "Red", equal_position, "Clue 1: Brit lives in Red"),
        Constraint("Spaniard", "Dog", equal_position, "Clue 2: Spaniard owns Dog"),
        Constraint("Coffee", "Green", equal_position, "Clue 3: Coffee in Green"),
        Constraint("Ukrainian", "Tea", equal_position, "Clue 4: Ukrainian drinks Tea"),
        Constraint("OldGold", "Snails", equal_position, "Clue 6: Old Gold owns Snails"),
        Constraint("Kools", "Yellow", equal_position, "Clue 7: Kools in Yellow"),
        Constraint(
            "LuckyStrike",
            "OrangeJuice",
            equal_position,
            "Clue 12: Lucky Strike drinks Orange Juice",
        ),
        Constraint(
            "Japanese",
            "Parliaments",
            equal_position,
            "Clue 13: Japanese smokes Parliaments",
        ),
    ]

    constraints += build_relative_constraints()
    constraints += build_all_different_constraints()
    return CSP(variables, domains, constraints)


def ac3(csp: CSP) -> bool:
    """Reduce domains with AC-3. Returns False if any domain becomes empty."""

    queue = deque((c.left, c.right) for c in csp.constraints)
    queue.extend((c.right, c.left) for c in csp.constraints)

    while queue:
        xi, xj = queue.popleft()
        if revise(csp, xi, xj):
            if not csp.domains[xi]:
                return False
            for neighbor in neighbors(csp, xi) - {xj}:
                queue.append((neighbor, xi))
    return True


def revise(csp: CSP, xi: str, xj: str) -> bool:
    """Remove values from Xi that have no valid partner in Xj."""

    related = constraints_between(csp, xi, xj)
    if not related:
        return False

    old_domain = set(csp.domains[xi])
    csp.domains[xi] = {
        x
        for x in old_domain
        if any(
            all(constraint.accepts(xi, x, y) for constraint in related)
            for y in csp.domains[xj]
        )
    }
    return csp.domains[xi] != old_domain


def constraints_between(csp: CSP, left: str, right: str) -> list[Constraint]:
    return [
        constraint
        for constraint in csp.constraints
        if {constraint.left, constraint.right} == {left, right}
    ]


def neighbors(csp: CSP, variable: str) -> set[str]:
    result: set[str] = set()
    for constraint in csp.constraints:
        if constraint.left == variable:
            result.add(constraint.right)
        elif constraint.right == variable:
            result.add(constraint.left)
    return result


def backtracking_search(csp: CSP) -> Assignment | None:
    domains = copy_domains(csp.domains)
    working = CSP(csp.variables, domains, csp.constraints)
    if not ac3(working):
        return None
    return backtrack({}, working)


def backtrack(assignment: Assignment, csp: CSP) -> Assignment | None:
    if len(assignment) == len(csp.variables):
        return dict(assignment)

    variable = select_mrv_variable(csp, assignment)
    for value in sorted(csp.domains[variable]):
        trial = {**assignment, variable: value}
        if not csp.is_consistent(trial):
            continue

        # Try this value, then let AC-3 prune domains before going deeper.
        new_domains = copy_domains(csp.domains)
        new_domains[variable] = {value}
        next_csp = CSP(csp.variables, new_domains, csp.constraints)

        if ac3(next_csp):
            result = backtrack(trial, next_csp)
            if result is not None:
                return result
    return None


def select_mrv_variable(csp: CSP, assignment: Assignment) -> str:
    unassigned = [v for v in csp.variables if v not in assignment]
    return min(unassigned, key=lambda variable: (len(csp.domains[variable]), variable))


def copy_domains(domains: dict[str, set[HousePosition]]) -> dict[str, set[HousePosition]]:
    return {variable: set(values) for variable, values in domains.items()}


def format_solution(solution: Assignment) -> str:
    rows = []
    for house in HOUSES:
        rows.append(
            {
                "House": str(house),
                "Color": value_at_house(COLORS, solution, house),
                "Nationality": value_at_house(NATIONALITIES, solution, house),
                "Drink": value_at_house(DRINKS, solution, house),
                "Tobacco": value_at_house(TOBACCOS, solution, house),
                "Pet": value_at_house(PETS, solution, house),
            }
        )

    headers = ("House", "Color", "Nationality", "Drink", "Tobacco", "Pet")
    widths = {
        header: max(len(header), *(len(row[header]) for row in rows))
        for header in headers
    }

    lines = ["Einstein's Riddle solution", ""]
    lines.append(" | ".join(header.ljust(widths[header]) for header in headers))
    lines.append("-+-".join("-" * widths[header] for header in headers))
    for row in rows:
        lines.append(" | ".join(row[header].ljust(widths[header]) for header in headers))

    lines += [
        "",
        f"Who owns the Zebra? {owner_of('Zebra', solution)}",
        f"Who drinks Water? {owner_of('Water', solution)}",
    ]
    return "\n".join(lines)


def value_at_house(group: tuple[str, ...], solution: Assignment, house: int) -> str:
    for value in group:
        if solution[value] == house:
            return display(value)
    return ""


def owner_of(attribute: str, solution: Assignment) -> str:
    house = solution[attribute]
    return value_at_house(NATIONALITIES, solution, house)


def display(value: str) -> str:
    return DISPLAY_NAMES.get(value, value)


def main() -> None:
    solution = backtracking_search(build_problem())
    if solution is None:
        raise SystemExit("No solution found.")
    print(format_solution(solution))


if __name__ == "__main__":
    main()
