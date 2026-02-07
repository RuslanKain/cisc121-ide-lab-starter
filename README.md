# CISC 121 — IDE Lab Starter (VS Code + Jupyter + Colab)

This repo is a **hands-on lab kit** to get you from *“I installed Python yesterday”* to *“I can confidently run `.py` files and `.ipynb` notebooks in VS Code (and Colab).”*

You’ll use this in a guided tutorial session. After the lab, you should be ready for an upcoming assignment that uses a **Jupyter Notebook**.

---

## What you’ll learn (in ~1 hour)

- Install Python and **verify it works**
- Use **VS Code** as a project workspace (open folder, terminal, run code)
- Understand **`.py` vs `.ipynb`** (and when to use each)
- Create and use a **virtual environment (venv)**
- Run a **Jupyter Notebook in VS Code**
- Run the **same notebook in Google Colab**
- A small end-cap on **debugging + testing** (just enough to get unstuck)

---

## Repo layout

```
cisc121-ide-lab-starter/
├─ docs/                 # the step-by-step student guide (short + practical)
├─ src/                  # Python files to run in VS Code
├─ notebooks/            # Jupyter notebooks to run in VS Code + Colab
├─ data/                 # small sample data files
└─ requirements.txt      # optional packages (for notebook support)
```

---

## Quick start (today’s “minimum viable setup”)

### 1) Install Python
Follow: **docs/01_install_python.md**

### 2) Install VS Code + extensions
Follow: **docs/02_vscode_setup.md**

### 3) Open this folder in VS Code
- In VS Code: **File → Open Folder…**
- Select the folder: `cisc121-ide-lab-starter`

### 4) Run a Python file
Follow: **docs/03_running_py_files.md**  
Suggested first run: `src/hello.py`

### 5) Run a notebook in VS Code
Follow: **docs/06_vscode_notebooks.md**  
Suggested first notebook: `notebooks/00_notebook_demo.ipynb`

### 6) Run the notebook in Colab
Follow: **docs/07_colab.md**

---

## Troubleshooting (the big 4)

**1) “It runs in terminal but not in VS Code.”**  
You probably selected the wrong Python interpreter in VS Code. See: `docs/02_vscode_setup.md`

**2) “ModuleNotFoundError”**  
You installed packages into one environment, but you’re running code in another. See: `docs/04_envs_venv.md`

**3) “Notebook won’t run / kernel missing.”**  
Your notebook kernel is not pointing at the environment you think it is. See: `docs/06_vscode_notebooks.md`

**4) “My notebook output is weird.”**  
Notebook state can get out of sync. Use: **Restart Kernel → Run All**. See: `docs/05_notebooks_vs_py.md`

---

## Official downloads (if you need them)
- Python: https://www.python.org/downloads/
- VS Code: https://code.visualstudio.com/download
- Colab: https://colab.google/

---

### If you’re a TA
See: `docs/TA_RUNBOOK.md` (the “minute-by-minute” script)
