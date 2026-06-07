"""Initial variables and domains for Einstein's Riddle."""

COLORS = ["Red", "Green", "Ivory", "Yellow", "Blue"]
NATIONALITIES = ["Brit", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
DRINKS = ["Coffee", "Tea", "Milk", "OrangeJuice", "Water"]
TOBACCOS = ["OldGold", "Kools", "Chesterfields", "LuckyStrike", "Parliaments"]
PETS = ["Dog", "Snails", "Fox", "Horse", "Zebra"]

VARIABLES = COLORS + NATIONALITIES + DRINKS + TOBACCOS + PETS
HOUSE_POSITIONS = [1, 2, 3, 4, 5]


def build_domains():
    """Create the initial domain for all 25 variables."""

    return {variable: HOUSE_POSITIONS[:] for variable in VARIABLES}


def apply_unary_constraints(domains):
    """Apply Clue 8 and Clue 9 to the domain table."""

    domains["Milk"] = [3]
    domains["Norwegian"] = [1]
    return domains


if __name__ == "__main__":
    domains = apply_unary_constraints(build_domains())
    print("Domain of Milk:", domains["Milk"])
    print("Domain of Norwegian:", domains["Norwegian"])
    print("Domain of Red:", domains["Red"])
