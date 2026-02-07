# 05 — `.py` vs `.ipynb` (Python files vs Notebooks)

## The big idea

### Python files (`.py`)
- Run top-to-bottom
- Great for **clean programs**, assignments, reusable code
- Easy to test and debug

### Jupyter notebooks (`.ipynb`)
- Run **cell-by-cell**
- Great for **exploration**, experiments, plots, learning
- But: they have **state** (you can run cells out of order)

---

## Notebook “state” in one sentence
A notebook remembers whatever you ran earlier — even if it’s not visible right now.

That’s why notebooks sometimes feel “haunted.”

---

## Best habits
- If something feels off: **Restart Kernel → Run All**
- Keep big logic in functions (even in notebooks)
- Don’t rely on “mystery variables” created 20 minutes ago
