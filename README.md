# AI-E-learning-1

Einstein's Riddle CSP Solver for exercise **3.3 Einstein's Riddle (The Zebra Puzzle)**.

The program solves the puzzle with:

- CSP modeling
- AC-3 domain pruning
- Backtracking search with MRV
- Relative constraints
- All-Different constraints

## Expected Answer

```text
Who owns the Zebra? Japanese
Who drinks Water? Norwegian
```

## How To Run

```powershell
python src/einstein_csp.py
```

If Windows does not recognize `python`, try:

```powershell
py -3 src/einstein_csp.py
```

## How To Run Tests

```powershell
python -m unittest
```

Fallback on Windows:

```powershell
py -3 -m unittest
```

## Repo Structure

- `src/einstein_csp.py`: CSP model, constraints, AC-3, Backtracking, and result formatting.
- `tests/test_einstein_csp.py`: tests for relative constraints, All-Different, AC-3, and final answer.
- `docs/khac_truong.md`: report notes for Khac Truong's assigned part.
- `docs/next_steps.md`: next steps for the remaining groups.

## CSP Model

Each attribute is represented as a variable whose value is the house position from left to right.

Examples:

- `Norwegian = 1`: Norwegian lives in the first house.
- `Milk = 3`: Milk is drunk in the middle house.
- `Green = Ivory + 1`: Green house is immediately right of Ivory house.
- `abs(Kools - Horse) == 1`: Kools is smoked next to the Horse.

All variables use the domain `{1, 2, 3, 4, 5}`.

## Khac Truong's Focus

In `src/einstein_csp.py`, focus on:

- `build_relative_constraints()`: clue 5, 10, 11, 14, 15.
- `build_all_different_constraints()`: prevents duplicate positions inside each group.
- `immediate_right()` and `next_to()`: formulas for position-based clues.
