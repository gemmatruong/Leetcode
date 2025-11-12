class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # columnNumber = 0
        # carry = 0
        # while len(columnTitle) > 0:
        #     columnNumber +=(ord(columnTitle[-1])-ord('A)+1)*(26**carry)
        #     carry += 1
        #     columnTitle = columnTitle[:-1]
        
        # return columnNumber

        columnNumber = 0
        for char in columnTitle:
            columnNumber = columnNumber*26 + ord(char) - ord('A') + 1
        return columnNumber

def main():
    sol = Solution()

    # 10 test cases
    test_cases = [
        ("A", 1),
        ("Z", 26),
        ("AA", 27),
        ("AB", 28),
        ("AZ", 52),
        ("BA", 53),
        ("ZY", 701),
        ("ZZ", 702),
        ("AAA", 703),
        ("ABC", 731),
    ]

    for title, expected in test_cases:
        result = sol.titleToNumber(title)
        print(f"Input: '{title}' → Output: {result} (Expected: {expected})",
              "✅" if result == expected else "❌")


if _name_ == "_main_":
    main()