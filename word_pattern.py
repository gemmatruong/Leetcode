class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Convert string of words into a list of words
        word_list = s.strip().split()

        # If two lengths are not the same, return False, no need to check further
        if len(pattern) != len(word_list):
            return False

        # Create a dictionary to map key from pattern to word in word_list
        mapping = {}
        word_seen = set()       # To check for words have been seen.

        for i in range(len(pattern)):
            char = pattern[i]
            word = word_list[i]
            # If a char is not a key in map, make it.
            if char not in mapping:
                # Make sure no two keys map to the same word
                if word in word_seen:
                    return False
                # Add key
                mapping[char] = word
                word_seen.add(word)
            else: # Key in map
                if word_list[i] != mapping[char]:
                    return False
        return True

def main():
    sol = Solution()

    # Test cases (pattern, s, expected)
    tests = [
        ("abba", "dog cat cat dog", True),          # matches pattern
        ("abba", "dog cat cat fish", False),        # last word mismatch
        ("aaaa", "dog dog dog dog", True),          # all same word
        ("abab", "dog cat dog cat", True),          # repeating pattern ok
        ("abab", "dog dog dog dog", False),         # same word mapped to two chars
        ("abba", "dog dog dog dog", False),         # two chars map to same word
        ("abc",  "apple banana cherry", True),      # all unique mapping
        ("abc",  "apple banana banana", False),     # duplicate word mismatch
        ("abc",  "apple banana", False),            # length mismatch
        ("",     "", True),                         # both empty (edge case)
    ]

    for i, (pattern, s, expected) in enumerate(tests, 1):
        result = sol.wordPattern(pattern, s)
        print(f"Test {i}: pattern='{pattern}', s='{s}' -> {result} (expected: {expected})")


if __name__ == "__main__":
    main()