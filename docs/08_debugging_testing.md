# 08 — Debugging + testing (small end-cap)

## Debugging: read the traceback like a detective
When Python crashes, it prints:
- the error type (e.g., `NameError`, `TypeError`)
- the file + line number
- the line of code

Start at the **bottom line** of the traceback:
- That’s the error Python is complaining about.

---

## VS Code: one breakpoint demo
In a `.py` file:
1) Click left of a line number to set a **red dot** (breakpoint)
2) Run → **Start Debugging**
3) Step through and watch variables change

This is how you make bugs show themselves.

---

## Testing: `assert` is the smallest unit of confidence

In `src/math_demo.py`, you’ll see tests like:

```python
assert add(2, 3) == 5
```

If the assertion fails, Python stops and tells you where.
That’s a mini test.
