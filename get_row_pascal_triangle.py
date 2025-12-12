from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # WAY 1: Using Generate function
        # def generate(numRows):
        #     if numRows == 1:
        #         return [[1]]
        #     if numRows == 2:
        #         return [[1], [1,1]]

        #     result = [[1], [1,1]]

        #     for i in range(2, numRows):
        #         # initialize a row with (i+1) column. Value of each column is 1
        #         row = [1] * (i+1)   
                
        #         # Loop goes from 2nd cell to (i-1)th cell in a row. 
        #         # i is the length of that row
        #         # the first and the last cells of the row are 1s by default
        #         for j in range(1, i):
        #             # each cell is a sum of the two cells above it.
        #             row[j] = result[i-1][j-1] + result[i-1][j]
        #         result.append(row)
        #     return result
        # return generate(rowIndex+1)[rowIndex]

        row = [1] * (rowIndex+1)
        for i in range(2, rowIndex + 1):
            for j in range(i-1, 0, -1):
                row[j] += row[j-1]
        return row
    
def main():
    sol = Solution()
    
    test_cases = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        10,
        33
    ]
    
    for idx in test_cases:
        print(f"rowIndex = {idx}")
        print(sol.getRow(idx))
        print("-" * 40)


if __name__ == "__main__":
    main()
