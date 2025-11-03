class Solution:
    def repeatedCharacter(self, s: str) -> str:
        occurence = {}

        for char in s:
            if char not in occurence:
                occurence[char] = 1
            else:
                return char
            
def main():
    sol = Solution()

    test_cases = [
        "abccba",          # 'c' repeats first
        "abcdefa",         # 'a' repeats first
        "abcdd",           # 'd' repeats first
        "aabbcc",          # 'a' repeats first
        "abcdeff",         # 'f' repeats first
        "xyzxyz",          # 'x' repeats first
        "a",               # No repeated char → should return None
        "abca",            # 'a' repeats first
        "abcdedcba",       # 'd' repeats first
        "redivider",       # 'r' repeats first
    ]

    for i, s in enumerate(test_cases, 1):
        result = sol.repeatedCharacter(s)
        print(f"Test case {i}: Input = '{s}' → First repeated character: {result}")


if __name__ == "__main__":
    main()