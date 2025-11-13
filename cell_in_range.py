from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        cells = []
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r1 = letters.find(s[0])
        r2 = letters.find(s[-2])

        for char in letters[r1:r2+1]:
            for i in range(int(s[1]), int(s[-1])+1):
                cells.append(char + str(i))
        
        return cells

def main():
    sol = Solution()
    
    test_cases = [
        "A1:C3",  # small 3x3 range
        "A1:A1",  # single cell
        "B2:B5",  # single column, multiple rows
        "C3:F3",  # single row, multiple columns
        "A1:B2",  # 2x2 grid
        "D4:E6",  # medium range
        "X1:Z2",  # range near end of alphabet
        "A9:C9",  # same row, different columns
        "M3:O5",  # middle range
        "A1:Z1"   # entire first row across alphabet
    ]

    for i, s in enumerate(test_cases, 1):
        result = sol.cellsInRange(s)
        print(f"Test {i}: {s} -> {result}")


if __name__ == "__main__":
    main()