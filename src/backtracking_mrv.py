# Einstein's Zebra Puzzle
# Backtracking + MRV

houses = [1, 2, 3, 4, 5]

colors = ["Red", "Green", "Ivory", "Yellow", "Blue"]
nations = ["Brit", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
drinks = ["Coffee", "Tea", "Milk", "OrangeJuice", "Water"]
smokes = ["OldGold", "Kools", "Chesterfields", "LuckyStrike", "Parliaments"]
pets = ["Dog", "Snails", "Fox", "Horse", "Zebra"]

variables = colors + nations + drinks + smokes + pets

domains = {v: houses[:] for v in variables}

# Unary Constraints
domains["Milk"] = [3]
domains["Norwegian"] = [1]


def check_constraints(assignment):

    def eq(a, b):
        return (
            a in assignment and
            b in assignment and
            assignment[a] == assignment[b]
        )

    # AllDifferent
    groups = [colors, nations, drinks, smokes, pets]

    for group in groups:
        vals = []

        for x in group:
            if x in assignment:
                vals.append(assignment[x])

        if len(vals) != len(set(vals)):
            return False

    # Clue 1
    if "Brit" in assignment and "Red" in assignment:
        if assignment["Brit"] != assignment["Red"]:
            return False

    # Clue 2
    if "Spaniard" in assignment and "Dog" in assignment:
        if assignment["Spaniard"] != assignment["Dog"]:
            return False

    # Clue 3
    if "Coffee" in assignment and "Green" in assignment:
        if assignment["Coffee"] != assignment["Green"]:
            return False

    # Clue 4
    if "Ukrainian" in assignment and "Tea" in assignment:
        if assignment["Ukrainian"] != assignment["Tea"]:
            return False

    # Clue 5
    if "Ivory" in assignment and "Green" in assignment:
        if assignment["Green"] != assignment["Ivory"] + 1:
            return False

    # Clue 6
    if "OldGold" in assignment and "Snails" in assignment:
        if assignment["OldGold"] != assignment["Snails"]:
            return False

    # Clue 7
    if "Kools" in assignment and "Yellow" in assignment:
        if assignment["Kools"] != assignment["Yellow"]:
            return False

    # Clue 10
    if "Chesterfields" in assignment and "Fox" in assignment:
        if abs(
            assignment["Chesterfields"] -
            assignment["Fox"]
        ) != 1:
            return False

    # Clue 11
    if "Kools" in assignment and "Horse" in assignment:
        if abs(
            assignment["Kools"] -
            assignment["Horse"]
        ) != 1:
            return False

    # Clue 12
    if "LuckyStrike" in assignment and "OrangeJuice" in assignment:
        if assignment["LuckyStrike"] != assignment["OrangeJuice"]:
            return False

    # Clue 13
    if "Japanese" in assignment and "Parliaments" in assignment:
        if assignment["Japanese"] != assignment["Parliaments"]:
            return False

    # Clue 14
    if "Norwegian" in assignment and "Blue" in assignment:
        if abs(
            assignment["Norwegian"] -
            assignment["Blue"]
        ) != 1:
            return False

    # Clue 15
    if "Chesterfields" in assignment and "Water" in assignment:
        if abs(
            assignment["Chesterfields"] -
            assignment["Water"]
        ) != 1:
            return False

    return True


# MRV
def select_unassigned_variable(assignment):

    unassigned = [
        v for v in variables
        if v not in assignment
    ]

    return min(
        unassigned,
        key=lambda v: len(domains[v])
    )


def backtrack(assignment):

    if len(assignment) == len(variables):
        return assignment

    var = select_unassigned_variable(assignment)

    for value in domains[var]:

        assignment[var] = value

        if check_constraints(assignment):

            result = backtrack(assignment)

            if result:
                return result

        del assignment[var]

    return None


def solve():

    solution = backtrack({})

    zebra_owner = None
    water_drinker = None

    for nat in nations:

        house_nat = solution[nat]

        for pet in pets:
            if pet == "Zebra" and solution[pet] == house_nat:
                zebra_owner = nat

        for drink in drinks:
            if drink == "Water" and solution[drink] == house_nat:
                water_drinker = nat

    return zebra_owner, water_drinker


if __name__ == "__main__":

    zebra_owner, water_drinker = solve()

    print("Owner of Zebra :", zebra_owner)
    print("Drinks Water   :", water_drinker)