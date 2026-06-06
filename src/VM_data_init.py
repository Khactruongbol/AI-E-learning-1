
# 1. Initialize data structure for 25 variables and their domains (1-5)
variables = [
    # Colors
    'Red', 'Green', 'Ivory', 'Yellow', 'Blue',
    # Nationalities
    'Brit', 'Spaniard', 'Ukrainian', 'Norwegian', 'Japanese',
    # Drinks
    'Coffee', 'Tea', 'Milk', 'OrangeJuice', 'Water',
    # Tobacco
    'OldGold', 'Kools', 'Chesterfields', 'LuckyStrike', 'Parliaments',
    # Pets
    'Dog', 'Snails', 'Fox', 'Horse', 'Zebra'
]

# Initially, each variable can be in any house from 1 to 5
domains = {var: [1, 2, 3, 4, 5] for var in variables}

# 2. Function to apply basic unary constraints (Clue 8 & 9)
def apply_unary_constraints(domains):
    """
    Apply unary constraints to narrow down the domains from the start.
    """
    # Clue 8: Milk is drunk in the middle house
    domains['Milk'] = [3]
    
    # Clue 9: The Norwegian lives in the first house
    domains['Norwegian'] = [1]
    
    return domains

# Test initialization
domains = apply_unary_constraints(domains)

# Print results
if __name__ == "__main__":
    print("Domain of Milk after initialization:", domains['Milk'])
    print("Domain of Norwegian after initialization:", domains['Norwegian'])
    print("Domain of Red (no constraints yet):", domains['Red'])