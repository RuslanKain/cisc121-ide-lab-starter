# 04 — Environments (venv) — just enough to be dangerous

## Goal
Create an isolated environment so packages don’t get messy.

Think of an environment as a **bubble**:
- Python version (sometimes)
- installed packages
- project-specific setup

---

## Create a venv (recommended)

From the repo folder:

### Windows (PowerShell)
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should now see `(.venv)` at the start of your terminal prompt.

---

## Install optional packages

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Tell VS Code to use the venv

- Ctrl+Shift+P → **Python: Select Interpreter**
- Pick the one inside `.venv`

---

## Brief note: Anaconda / conda (optional alternative)

Conda is popular because it manages:
- environments
- packages (including non-Python dependencies)

If you already use Anaconda, that’s fine — just make sure VS Code uses the same environment.

Download: https://www.anaconda.com/download
