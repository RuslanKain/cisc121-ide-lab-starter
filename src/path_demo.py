"""path_demo.py

A quick demo of file paths:
- reads a file from the data/ folder
"""

from pathlib import Path

def main():
    here = Path(__file__).resolve().parent
    data_file = here.parent / "data" / "numbers.txt"

    text = data_file.read_text().strip()
    nums = [int(x) for x in text.split()]
    print(f"Read {len(nums)} numbers from {data_file}")
    print(f"Sum = {sum(nums)}")

if __name__ == "__main__":
    main()
