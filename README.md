# AI-E-learning-1

Source code for Exercise 3.3: Einstein's Riddle / Zebra Puzzle.

## Requirements

- Python 3.10 or newer
- No external Python packages are required for the source code

## Run The Program

```powershell
python src/main.py
```

If Windows does not recognize `python`, use:

```powershell
py -3 src/main.py
```

Expected final answers:

```text
Who owns the Zebra? Japanese
Who drinks Water? Norwegian
```

## Run Tests

```powershell
python -m unittest
```

Windows fallback:

```powershell
py -3 -m unittest
```

## Useful Source Files

- `src/main.py`: main runner.
- `src/einstein_csp.py`: complete CSP model, AC-3, Backtracking, and output formatting.
- `src/data_init.py`: variables and initial domains.
- `src/clue_checks.py`: basic clue checks.
- `src/ac3_algorithm.py`: AC-3 entry point.
- `src/backtracking_mrv.py`: Backtracking and MRV implementation.

## Notes

Generated files such as `__pycache__`, `.pyc`, and `.log` are ignored by Git.
