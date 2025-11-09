class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert string to array of characters
        s_arr = list(s)
        length = len(s_arr)
        
        for i in range(0, length, 2 * k):
            s_arr[i:i + k] = reversed(s_arr[i:i + k])

        return "".join(s_arr)

def main():
    sol = Solution()

    test_cases = [
        # (input_string, k, expected_output)
        ("abcdefg", 2, "bacdfeg"),             # Example from LeetCode
        ("abcd", 2, "bacd"),                   # Even length, multiple of k
        ("a", 2, "a"),                         # Single char
        ("ab", 2, "ba"),                       # Exactly k characters
        ("abc", 2, "bac"),                     # Less than 2k but > k
        ("abcd", 3, "cbad"),                   # k > half of length
        ("abcdef", 3, "cbadef"),               # Exact 2k = 6
        ("abcdefghi", 3, "cbadefihg"),         # Length > 2k, multiple blocks
        ("abcdefghij", 4, "dcbaefghji"),       # Partial 2k at end
        ("abcdefghijklm", 5, "edcbafghijmlk"), # Edge: remainder less than k
        ("abcdefghijklmnop", 2, "bacdfeghjiklnmop"), # Many small blocks
    ]

    for i, (s, k, expected) in enumerate(test_cases, 1):
        result = sol.reverseStr(s, k)
        print(f"Test {i}: s='{s}', k={k}")
        print(f"→ Output:   {result}")
        print(f"→ Expected: {expected}")
        print("✅ Pass\n" if result == expected else "❌ Fail\n")


if __name__ == "__main__":
    main()