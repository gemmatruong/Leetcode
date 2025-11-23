from typing import List

class Solution:
    @staticmethod
    def isPattern(pattern, s):
        # If two lengths are not the same, return False, no need to check further
        if len(pattern) != len(s):
            return False

        # Create a dictionary to map key from pattern to word in word_list
        mapping = {}
        seen = set()       # To check for words have been seen.

        for p, w in zip(pattern, s):
            if p not in mapping:
                if w in seen:
                    return False
                mapping[p] = w
                seen.add(w)
            else:
                if mapping[p] != w:
                    return False  
        return True

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            if Solution.isPattern(pattern, word):
                result.append(word)
        return result

        # def encode(w):
        #     mp = {}
        #     res = []
        #     nxt = 0
        #     for c in w:
        #         if c not in mp:
        #             mp[c] = nxt
        #             nxt += 1
        #         res.append(mp[c])
        #     return res

        # key = encode(pattern)
        # return [w for w in words if encode(w) == key]

def main():
    sol = Solution()

    # (words, pattern, expected result)
    tests = [
        (["abc","deq","mee","aqq","dkd","ccc"], "abb", ["mee","aqq"]),                    # example case
        (["a","b","c"], "a", ["a","b","c"]),                                             # single character mapping
        (["xyz","xyy","yyx","yxx"], "foo", ["xyy","yyx"]),                               # repeating pattern
        (["abc","cba","xyx","yxx","yyx"], "aba", ["xyx"]),                               # symmetry match
        (["aa","bb","cc","cd"], "dd", ["aa","bb","cc"]),                                 # all match except one
        (["mno","pqr","stu"], "xyz", ["mno","pqr","stu"]),                               # all match unique
        (["ab","cd","ee","ff"], "gg", ["ee","ff"]),                                      # avoid duplicate mapping
        (["aba","baa","aaa","ccc"], "xyz", []),                                          # mixed matches
        ([], "abc", []),                                                                 # empty word list
        (["abcd","deee","ffff","xyyx"], "abba", ["xyyx"]),                               # 4-letter mapping
    ]

    for i, (words, pattern, expected) in enumerate(tests, 1):
        result = sol.findAndReplacePattern(words, pattern)
        print(f"Test {i}: pattern='{pattern}', words={words}")
        print(f" → Result:   {result}")
        print(f" → Expected: {expected}")
        print(f" → Pass:     {result == expected}\n")


if __name__ == "__main__":
    main()