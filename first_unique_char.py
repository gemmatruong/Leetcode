from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Use map to count the occurence of each characters.
        # char_count = {}

        # for char in s:
        #     char_count[char] = char_count.get(char, 0) + 1
        
        # for i, char in enumerate(s):
        #     if char_count[char] == 1:
        #         return i
        # return -1
        #-----------------------------------------------------------

        # Use counter()
        char_count = Counter(s)

        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        return -1

def main():
    sol = Solution()
    test_cases = [
        ("leetcode", 0),           # 'l' is unique, index 0
        ("loveleetcode", 2),       # 'v' is first unique, index 2
        ("aabb", -1),              # no unique char
        ("", -1),                  # empty string
        ("z", 0),                  # single character
        ("aabbccdde", 8),          # 'e' is unique at end
        ("aabccbd", 6),            # 'd' is unique at last index
        ("abcabc", -1),            # all characters repeat
        ("swiss", 1),              # 'w' unique at index 1
        ("redivider", 4),          # palindrome, 'v' unique at index 4
        ("teeter", 2),             # 'e' repeats, 't' repeats, 'r' unique at 5
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        result = sol.firstUniqChar(s)
        print(f"Test {i}: Input='{s}' | Output={result} | Expected={expected} | {'✅ Pass' if result == expected else '❌ Fail'}")


if __name__ == "__main__":
    main()