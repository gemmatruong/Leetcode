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

