from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(1,int(len(s)/2)+1,1):
            temp = s[i-1]
            s[i-1] = s[-i]
            s[-i] = temp

def main():
    sol = Solution()

    test_cases = [
        list("hello"),
        list("Python"),
        list("racecar"),
        list("a"),
        list("ab"),
        list("abcd"),
        list("OpenAI"),
        list("ChatGPT"),
        list("12345"),
        list("!@#$$#@!")
    ]

    for i, test in enumerate(test_cases, 1):
        original = test.copy()
        sol.reverseString(test)
        print(f"Test case {i}: {''.join(original)} -> {''.join(test)}")


if __name__ == "__main__":
    main()