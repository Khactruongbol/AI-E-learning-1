colors = ["Red", "Green", "Ivory", "Yellow", "Blue"]

nationalities = [
    "English",
    "Spanish",
    "Ukrainian",
    "Norwegian",
    "Japanese"
]

drinks = [
    "Coffee",
    "Tea",
    "Milk",
    "OrangeJuice",
    "Water"
]

tobaccos = [
    "OldGold",
    "Kools",
    "Chesterfields",
    "LuckyStrike",
    "Parliaments"
]

pets = [
    "Dog",
    "Snails",
    "Fox",
    "Horse",
    "Zebra"
]


house = {
    "Color": None,
    "Nationality": None,
    "Drink": None,
    "Tobacco": None,
    "Pet": None
}
house_test = {
    "Color": "Red",
    "Nationality": "English",
    "Drink": "Tea",
    "Tobacco": "Kools",
    "Pet": "Dog"
}
houses = [house.copy() for _ in range(5)]
def check_clue1(house):
    if house["Nationality"] == "English":
        return house["Color"] == "Red"
    return True
print("Clue1:", check_clue1(house_test))
def check_clue2(house): 
    if house["Nationality"] == "Spanish": 
        return house["Pet"] == "Dog" 
    return True
print("Clue2:", check_clue2(house_test))
def check_clue3(house): 
    if house["Color"] == "Green": 
        return house["Drink"] == "Coffee" 
    return True
print("Clue3:", check_clue3(house_test))
def check_clue4(house): 
    if house["Nationality"] == "Ukrainian": 
        return house["Drink"] == "Tea" 
    return True
print("Clue4:", check_clue4(house_test))
def check_clue6(house): 
    if house["Tobacco"] == "OldGold": 
        return house["Pet"] == "Snails" 
    return True
print("Clue6:", check_clue6(house_test))
def check_clue7(house): 
    if house["Tobacco"] == "Kools": 
        return house["Color"] == "Yellow" 
    return True
print("Clue7:", check_clue7(house_test))
def check_clue8(houses): 
    return houses[2]["Drink"] == "Milk"
print("Clue8:", check_clue8(houses))
def check_clue9(houses): 
    return houses[0]["Nationality"] == "Norwegian"
print("Clue9:", check_clue9(houses))
def all_different(values): 
    values = [v for v in values if v is not None] 
    return len(values) == len(set(values))
