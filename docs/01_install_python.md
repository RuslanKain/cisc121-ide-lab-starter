# 01 — Install Python + verify it works

## Goal
By the end of this section, you can run Python and see output.

---

## Download Python (official)
Use: https://www.python.org/downloads/

### Windows notes (important)
During install, **check the box**:
- ✅ *Add Python to PATH*

Then install with defaults.

### macOS
Install from python.org, or use your course’s recommended installer if provided.

### Linux
Python is often already installed. If you need it:
- Use your distro package manager (e.g., `apt`, `dnf`) based on TA instructions.

---

## Verify the install

Open a terminal:

### Windows
- Start Menu → type **Command Prompt** (or PowerShell)

### macOS / Linux
- Open **Terminal**

Run:

```bash
python --version
```

If that fails on macOS/Linux, try:

```bash
python3 --version
```

You should see something like: `Python 3.x.x`

---

## Run a one-liner

```bash
python -c "print('Python is working ✅')"
```

If that prints correctly, you’re good.
