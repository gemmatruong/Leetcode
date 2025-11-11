class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        letters = [chr(65+i) for i in range(26)]

        while columnNumber > 0:
            columnNumber -= 1
            title = letters[columnNumber%26] + title
            columnNumber //= 26
        
        return title

def main():
    solution = Solution()
    
    # 10 test cases
    test_cases = [
        1,       # A
        26,      # Z
        27,      # AA
        28,      # AB
        52,      # AZ
        53,      # BA
        701,     # ZY
        702,     # ZZ
        703,     # AAA
        18278    # ZZZ
    ]
    
    for num in test_cases:
        result = solution.convertToTitle(num)
        print(f"Input: {num:<6} → Output: {result}")


if __name__ == "__main__":
    main()