# TA_RUNBOOK — 60-minute lab script (VS Code + Notebooks + Colab)

## Outcomes for students (by end)
- They can run `.py` in VS Code (Run button + terminal)
- They understand `.py` vs `.ipynb`
- They can run `.ipynb` in VS Code and in Colab
- They understand the *basic* idea of environments and interpreter selection

---

## Prep (before the session)
- Confirm Python + VS Code are installed on your machine
- Pull up this repo
- Be ready to screen-share:
  - VS Code (Explorer + Terminal)
  - A notebook open in VS Code
  - Colab in browser

---

## Minute-by-minute

### 0–5 — What we’re doing today
- Two workflows:
  1) run `.py`
  2) run `.ipynb`
- One concept to keep repeating:
  - interpreter / environment selection

### 5–15 — Install + verify Python
Have them follow: `docs/01_install_python.md`  
Quick checks:
- `python --version`
- `python -c "print('Python is working ✅')"`

### 15–30 — VS Code basics + run a `.py`
Have them follow: `docs/02_vscode_setup.md` + `docs/03_running_py_files.md`

Student drills:
- Run `src/hello.py` (Run button)
- Run `python src/hello.py` (terminal)
- Introduce one deliberate mistake:
  - remove a quote → run → fix syntax error → re-run

### 30–40 — venv (lightweight)
Follow: `docs/04_envs_venv.md`

Student drills:
- create `.venv`
- activate it
- select it as interpreter in VS Code

### 40–52 — Notebooks in VS Code
Follow: `docs/06_vscode_notebooks.md`

Student drills in notebook:
- run cells top-to-bottom
- then intentionally run out of order
- recover using **Restart Kernel → Run All**

### 52–58 — Colab
Follow: `docs/07_colab.md`

Student drills:
- upload notebook
- run all
- save a copy

### 58–60 — tiny debugging/testing teaser
- Show a breakpoint on `src/buggy_average.py` OR read one traceback
- Show two `assert`s in `src/math_demo.py`

---

## If students get stuck (triage)
1) Interpreter mismatch (most common)
2) Kernel mismatch (notebooks)
3) Notebook state (restart + run all)
4) PATH issue (Windows install box was skipped)
