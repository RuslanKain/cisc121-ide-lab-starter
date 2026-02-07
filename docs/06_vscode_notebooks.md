# 06 — Run a Jupyter Notebook in VS Code

## Goal
Open an `.ipynb` file and run cells using the **correct kernel**.

---

## Open the notebook
Open: `notebooks/00_notebook_demo.ipynb`

You should see:
- Cells
- Play/run icons
- Output area under cells

---

## Pick a kernel (the notebook’s Python)

Top-right of the notebook, you’ll see a kernel picker.

Choose:
- your `.venv` interpreter (recommended), or
- your system Python (if you skipped venv)

If you don’t see any kernels:
1) Confirm the **Jupyter extension** is installed
2) Confirm you installed requirements (`pip install -r requirements.txt`)
3) Re-open VS Code

---

## Run cells
- Run the first cell
- Then follow the notebook instructions

At one point you’ll intentionally run things out of order to see what happens.
That’s the point. 🙂

---

## Reset when things get weird
- “Restart” the kernel
- “Run All”
