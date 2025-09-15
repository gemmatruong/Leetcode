""" Given a string s consisting of words and spaces, return the length of the last word in the string.
    A word is a maximal substring consisting of non-space characters only.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0 or len(s) == 1 or (' ' not in s):
            return len(s)
        i = -1
        length = 0
        while s[i] != ' ':
            length += 1
            i -= 1
        return length

def main():
    s = Solution()
    print("- Length of last word -")
    print(f"'Hello World': {s.lengthOfLastWord("Hello World")}")  # Output: 5
    print(f"'   fly me   to   the moon  ': {s.lengthOfLastWord("   fly me   to   the moon  ")}")  # Output: 4
    print(f"'luffy is still joyboy': {s.lengthOfLastWord("luffy is still joyboy")}")  # Output: 6
    print(f"'a': {s.lengthOfLastWord("a")}")  # Output: 1
    print(f"'a ': {s.lengthOfLastWord("a ")}")  # Output: 1
    print(f"'  ': {s.lengthOfLastWord(" ")}")  # Output: 0
    print(f"'': {s.lengthOfLastWord("")}")  # Output: 0
    print(f"'day': {s.lengthOfLastWord("day")}")  # Output: 3

if __name__ == "__main__":
    main()