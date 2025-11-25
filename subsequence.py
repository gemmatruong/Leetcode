class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # WAY 2: O(n). Use 2 indexes
        s_idx = 0
        t_idx = 0

        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1
        return s_idx == len(s)

def main():
    sol = Solution()

    test_cases = [
        ("abc", "ahbgdc"),       # True - standard subsequence
        ("axc", "ahbgdc"),       # False - 'x' missing
        ("", "ahbgdc"),          # True - empty string is subsequence of any
        ("abc", ""),             # False - non-empty can't be subsequence of empty
        ("abc", "abc"),          # True - exact match
        ("abc", "aabbcc"),       # True - repeating letters but still valid
        ("aaaa", "aa"),          # False - not enough 'a's
        ("ace", "abcde"),        # True - skipping characters in between
        ("aec", "abcde"),        # False - wrong order
        ("hello", "hleolworld"), # True - letters appear in correct order
    ]

    for i, (s, t) in enumerate(test_cases, 1):
        result = sol.isSubsequence(s, t)
        print(f"Test Case {i}: isSubsequence('{s}', '{t}') -> {result}")


if __name__ == "__main__":
    main()