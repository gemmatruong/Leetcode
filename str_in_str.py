class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        # this is the slide window approach
        for i in range(len(haystack) - len(needle) + 1): # check until the last possible starting point
            if haystack[i:i+len(needle)] == needle:      # check the substring
                return i
        return -1

def main():
    sol = Solution()
    
    # Test cases
    haystack1, needle1 = "hello", "ll"
    haystack2, needle2 = "aaaaa", "bba"
    haystack3, needle3 = "", ""
    haystack4, needle4 = "abc", ""
    haystack5, needle5 = "abc", "c"
    
    assert sol.strStr(haystack1, needle1) == 2
    assert sol.strStr(haystack2, needle2) == -1
    assert sol.strStr(haystack3, needle3) == 0
    assert sol.strStr(haystack4, needle4) == 0
    assert sol.strStr(haystack5, needle5) == 2
    
    print("All tests passed.")

if __name__ == "__main__":
    main()