# 03 — Running `.py` files in VS Code

## Goal
Run Python code **two ways**:
1) VS Code “Run” button (easy)
2) Terminal command (portable)

---

## Option A — Run button (recommended for beginners)

1) Open `src/hello.py`
2) Click the **Run ▶** button (top right)

If VS Code asks you to select an interpreter, do it.

---

## Option B — Terminal (what you’ll use when tools get fancy)

In VS Code: **Terminal → New Terminal**

Run:

```bash
python src/hello.py
```

If that fails, try:

```bash
python3 src/hello.py
```

---

## Common gotcha: running the wrong file
Make sure you’re in the **repo folder** and you typed the correct path.
