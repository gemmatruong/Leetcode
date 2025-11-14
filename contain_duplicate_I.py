from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)

        if len(nums_set) != len(nums):
            return True
        return False

def main():
    sol = Solution()

    # Test cases
    test_cases = [
        ([1, 2, 3, 1], True),           # duplicate 1
        ([1, 2, 3, 4], False),          # all unique
        ([1, 1, 1, 1], True),           # all same
        ([0], False),                   # single element
        ([], False),                    # empty list
        ([-1, -2, -3, -1], True),       # negative duplicates
        ([10, 20, 30, 40, 50], False),  # all distinct
        ([5, 5, 6, 7, 8, 5], True),     # multiple duplicates
        ([100000, 99999, 100000], True),# large number duplicate
        (list(range(10000)) + [9999], True)  # large input with one duplicate
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = sol.containsDuplicate(nums)
        print(f"Test {i}: Input={nums[:10]}{'...' if len(nums) > 10 else ''} | "
              f"Expected={expected} | Output={result} | {'✅' if result == expected else '❌'}")


if __name__ == "__main__":
    main()