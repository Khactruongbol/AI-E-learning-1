"""Basic clue checks for house-record style reasoning."""


def check_clue1(house):
    return house["Nationality"] != "Brit" or house["Color"] == "Red"


def check_clue2(house):
    return house["Nationality"] != "Spaniard" or house["Pet"] == "Dog"


def check_clue3(house):
    return house["Color"] != "Green" or house["Drink"] == "Coffee"


def check_clue4(house):
    return house["Nationality"] != "Ukrainian" or house["Drink"] == "Tea"


def check_clue6(house):
    return house["Tobacco"] != "OldGold" or house["Pet"] == "Snails"


def check_clue7(house):
    return house["Tobacco"] != "Kools" or house["Color"] == "Yellow"


def check_clue8(houses):
    return houses[2]["Drink"] == "Milk"


def check_clue9(houses):
    return houses[0]["Nationality"] == "Norwegian"


def all_different(values):
    assigned_values = [value for value in values if value is not None]
    return len(assigned_values) == len(set(assigned_values))


if __name__ == "__main__":
    sample_house = {
        "Color": "Red",
        "Nationality": "Brit",
        "Drink": "Tea",
        "Tobacco": "Kools",
        "Pet": "Dog",
    }
    print("Clue 1:", check_clue1(sample_house))
    print("Clue 2:", check_clue2(sample_house))
