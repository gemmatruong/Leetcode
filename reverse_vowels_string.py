class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'o', 'e', 'u', 'i', 'A', 'O', 'E', 'U', 'I']

        s_arr = list(s)

        start = 0
        end = len(s_arr) - 1

        while start < end:
            if (s_arr[start] in vowels) and (s_arr[end] in vowels):
                s_arr[start], s_arr[end] = s_arr[end], s_arr[start]
                start += 1
                end -= 1
            elif s_arr[start] not in vowels:
                start += 1
            else:
                end -= 1

        s = "".join(s_arr)
        return s
        
def main():
    sol = Solution()

    test_cases = [
        ("hello", "holle"),          # simple case
        ("leetcode", "leotcede"),    # multiple vowels
        ("aA", "Aa"),                # two vowels, different cases
        ("programming", "prigrammong"), # mixed vowels
        ("sky", "sky"),              # no vowels
        ("", ""),                    # empty string
        ("AEIOU", "UOIEA"),          # all uppercase vowels
        ("Banana", "banana"),        # mixed case
        ("Reverse Vowels!", "Rivorse Vewels!"), # with punctuation
        ("Why so serious?", "Why so sorieus?")  # multiple vowels spaced out
    ]

    for i, (inp, expected) in enumerate(test_cases, 1):
        result = sol.reverseVowels(inp)
        print(f"Test case {i}: '{inp}' -> '{result}' | Expected: '{expected}' | {'✅' if result == expected else '❌'}")


if __name__ == "__main__":
    main()
