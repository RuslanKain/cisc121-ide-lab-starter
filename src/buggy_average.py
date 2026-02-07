"""buggy_average.py

A tiny program with a deliberate bug.

Your task (in the lab):
1) Run it
2) Observe the incorrect output
3) Fix the bug
4) Re-run to confirm it works
"""

def average(nums):
    # BUG: using integer division will silently truncate for many inputs
    # Example: (1 + 2) // 2  gives 1  instead of 1.5
    return sum(nums) // len(nums)

def main():
    nums = [1, 2, 3, 4]
    avg = average(nums)
    print(f"Numbers: {nums}")
    print(f"Average: {avg}")  # should be 2.5

if __name__ == "__main__":
    main()
