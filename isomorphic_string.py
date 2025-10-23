from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letter_dict = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in letter_dict:
                letter_dict[s[i]] = t[i]
            elif t[i] != letter_dict[s[i]]:
                return False
        values_count = Counter(letter_dict.values())
        
        print(values_count)

        for k in values_count:
            if values_count[k] > 1:
                return False
        return True

def main():
    sol = Solution()
    print(sol.isIsomorphic("badc", "baba")) 

if __name__ == "__main__":
    main()   