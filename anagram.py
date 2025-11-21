from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ''' 3 Ways to solve this problem'''
        # Way 1: use list and sorted() function

        # if len(s) != len(t):
        #     return False

        # s_list = list(s)
        # t_list = list(t)

        # if sorted(s_list) == sorted(t_list):
        #     return True
        # return False

        # Way 2: Use Counter library

        # s_count = Counter(s)
        # t_count = Counter(t)

        # return s_count == t_count

        # Way 3: Use set() and count() function
        if len(s) != len(t):
            return False
            
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True

def main():
    sol = Solution()

    test_cases = [
        ("anagram", "nagaram"),      # True
        ("rat", "car"),              # False
        ("listen", "silent"),        # True
        ("aaaa", "aaa"),             # False (different lengths)
        ("", ""),                    # True (both empty)
        ("aacc", "ccac"),            # False
        ("abc123", "321cba"),        # True (numbers + letters)
        ("Hello", "hello"),          # False (case sensitive)
        ("😀😃😄", "😄😃😀"),        # True (unicode emoji)
        ("triangle", "integral"),    # True
    ]

    for i, (s, t) in enumerate(test_cases, 1):
        result = sol.isAnagram(s, t)
        print(f"Test {i}: isAnagram({s!r}, {t!r}) = {result}")


if __name__ == "__main__":
    main()
