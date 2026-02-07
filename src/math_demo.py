"""math_demo.py

A tiny example of:
- writing small functions
- using assert as mini-tests
"""

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def main():
    # Mini tests (these should pass)
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert is_even(4) is True
    assert is_even(5) is False

    print("All asserts passed ✅")

if __name__ == "__main__":
    main()
