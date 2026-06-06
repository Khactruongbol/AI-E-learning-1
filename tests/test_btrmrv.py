
from backtracking_mrv import solve


def test_solution():

    zebra_owner, water_drinker = solve()

    assert zebra_owner == "Japanese"
    assert water_drinker == "Norwegian"

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()