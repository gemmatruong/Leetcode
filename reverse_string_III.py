class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        result_list = []

        for word in word_list:
            result_list.append(word[::-1])
        
        return " ".join(result_list)

def main():
    sol = Solution()

    test_cases = [
        # (input_string, expected_output)
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),  # Example from LeetCode
        ("God Ding", "doG gniD"),                                         # Simple two words
        ("a b c d", "a b c d"),                                           # Single letters
        ("hello", "olleh"),                                               # Single word
        ("  hello world  ", "olleh dlrow"),                               # Extra spaces trimmed by split()
        ("This is a test", "sihT si a tset"),                             # Normal sentence
        ("Python3 is fun!", "3nohtyP si !nuf"),                           # Word with number and punctuation
        ("  space   between   words  ", "ecaps neewteb sdrow"),           # Irregular spacing
        ("", ""),                                                         # Empty string
        ("single", "elgnis"),                                             # Single word edge case
        ("palindrome level noon", "emordnilap level noon"),               # Words that reverse interestingly
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        result = sol.reverseWords(s)
        print(f"Test {i}: s='{s}'")
        print(f"→ Output:   '{result}'")
        print(f"→ Expected: '{expected}'")
        print("✅ Pass\n" if result == expected else "❌ Fail\n")


if __name__ == "__main__":
    main()