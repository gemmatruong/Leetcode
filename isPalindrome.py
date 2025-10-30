class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(char.lower() for char in s if char.isalnum())

        start = 0
        end = len(new_s) - 1

        if len(new_s) in [0,1]:
            return True

        while start < end:
            if new_s[start] != new_s[end]:
                return False
            start += 1
            end -= 1
        return True

        #Faster way:
        # new_s = "".join(char.lower() for char in s if char.isalnum())
        # return new_s == new_s[::-1]

def main():
    sol = Solution()

    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("Madam", True),
        ("No lemon, no melon", True),
        ("Was it a car or a cat I saw?", True),
        ("12321", True),
        ("1231", False),
        ("Able was I, I saw elba", True),
    ]

    print("Running palindrome tests:\n")
    for i, (s, expected) in enumerate(test_cases, 1):
        result = sol.isPalindrome(s)
        status = "✅ Passed" if result == expected else "❌ Failed"
        print(f"Test {i:02}: {s!r:35} → {result} (Expected: {expected}) {status}")


if __name__ == "__main__":
    main()