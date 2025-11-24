from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Way 1: find a matched character in magazine, remove it. O(n)
        # Can't construct a string from a shorter string
        if len(ransomNote) > len(magazine):
            return False
        
        # Traverse through ransomNote
        for char in ransomNote:
            # A char can't be constructed from a list of chars if it isn't in that list
            if char not in magazine:
                return False
            idx = magazine.find(char)
            # Remove char in the magazine at that index
            magazine = magazine[:idx] + magazine[idx+1:]
        return True

        # ---------------------------------------------------------
        # Way 2: Use Counter(). O(n)
        # # Can't construct a string from a shorter string
        # if len(ransomNote) > len(magazine):
        #     return False

        # # Count the occurence of letters in magazine
        # letters_count = Counter(magazine)
        
        # for char in ransomNote:
        #     if char not in magazine:
        #         return False
        #     value = letters_count[char]
        #     if value == 0:
        #         return False
        #     letters_count[char] = value - 1
        # return True