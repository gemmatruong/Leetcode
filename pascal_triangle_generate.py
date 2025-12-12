from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]

        result = [[1], [1,1]]

        for i in range(2, numRows):
            # initialize a row with (i+1) column. Value of each column is 1
            row = [1] * (i+1)   
            
            # Loop goes from 2nd cell to (i-1)th cell in a row. 
            # i is the length of that row
            # the first and the last cells of the row are 1s by default
            for j in range(1, i):
                # each cell is a sum of the two cells above it.
                row[j] = result[i-1][j-1] + result[i-1][j]
            result.append(row)
        return result

def main():
    sol = Solution()

    print("TEST CASES FOR generate():\n")

    # 1. numRows = 1
    print(sol.generate(1))
    # Expected: [[1]]

    # 2. numRows = 2
    print(sol.generate(2))
    # Expected: [[1], [1,1]]

    # 3. numRows = 3
    print(sol.generate(3))
    # Expected: [[1],[1,1],[1,2,1]]

    # 4. numRows = 4
    print(sol.generate(4))
    # Expected: [[1],[1,1],[1,2,1],[1,3,3,1]]

    # 5. numRows = 5 (classic)
    print(sol.generate(5))
    # Expected: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    # 6. numRows = 6
    print(sol.generate(6))
    # Expected last row: [1,5,10,10,5,1]

    # 7. numRows = 10
    print(sol.generate(10))
    # Expected last row: [1,9,36,84,126,126,84,36,9,1]

    # 8. numRows = 0 (not in LeetCode, but edge case)
    # Your code does not explicitly handle numRows <= 0,
    # but this is a typical test.
    try:
        print(sol.generate(0))
    except Exception as e:
        print("Error:", e)
    # Expected: Error or empty (depending on how you choose)

    # 9. numRows = 15
    print(sol.generate(15)[-1])
    # Expected last row: coefficients of (x+y)^14

    # 10. numRows = 20 (performance check)
    triangle20 = sol.generate(20)
    print(triangle20[-1])
    # Expected: 20th row with 20 elements

main()
