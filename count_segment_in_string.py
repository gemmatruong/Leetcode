class Solution:
    def countSegments(self, s: str) -> int:
        s = " ".join(s.strip().split())
        if len(s) == 0:
            return 0
        count = 1
        for char in s.strip():
            if char.isspace():
                count += 1
        return count


def main():
    sol = Solution()
    test_cases = [
        "",                           # 0 segments
        "Hello",                      # 1 segment
        "Hello world",                # 2 segments
        "   Hello world   ",          # 2 segments (leading/trailing spaces)
        "Hello   world   test",       # 3 segments (extra spaces between)
        "   ",                        # 0 segments (only spaces)
        "a b c d e",                  # 5 segments (single characters)
        "OpenAI ChatGPT 5 model",     # 4 segments
        "Python  is   great",         # 3 segments
        " multiple    spaces   here ",# 3 segments
        "             "               # 0 segments
    ]

    for i, s in enumerate(test_cases, 1):
        result = sol.countSegments(s)
        print(f"Test case {i}: '{s}' -> {result}")


if __name__ == "__main__":
    main()