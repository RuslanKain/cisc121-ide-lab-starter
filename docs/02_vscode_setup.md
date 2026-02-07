# 02 — VS Code setup (Python + Jupyter)

## Goal
By the end of this section, VS Code can run Python code in **this folder**.

---

## Install VS Code
Download: https://code.visualstudio.com/download

---

## Install extensions (inside VS Code)

Open VS Code → Extensions (left sidebar) → install:

1) **Python** (by Microsoft)
2) **Jupyter** (by Microsoft)

---

## Open the project folder (not just one file)

In VS Code:
- **File → Open Folder…**
- Select: `cisc121-ide-lab-starter`

Why this matters:
- VS Code treats a folder as a “project”
- Paths, notebooks, and environments behave more predictably

---

## Select your Python interpreter

In VS Code:
- Press **Ctrl+Shift+P** (Cmd+Shift+P on Mac)
- Type: **Python: Select Interpreter**
- Choose the interpreter you installed (or your venv later)

You can confirm in the bottom-right status bar: it shows the selected Python.

---

## Quick sanity check

Open `src/hello.py` and run it (next doc explains how).
