from typing import List
"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""

class Solution:
    # Using the Boyer–Moore Voting Algorithm.
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        result = None

        for num in nums:
            if count == 0:
                result = num
                count = 1
            elif num == result:
                count += 1
            else:
                count -= 1
        return result

def main():
    print("=== Majority Element Finder ===\n")

    test_cases = [
        # Basic small cases
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1, 1, 1, 3, 3, 2, 1], 1),
        ([5, 5, 5, 5, 2, 3, 4], 5),
        ([6], 6),
        ([1, 1, 2], 1),

        # Majority at the end
        ([7, 8, 9, 7, 7, 7, 7], 7),

        # Majority at the beginning
        ([9, 9, 9, 9, 1, 2, 3, 4], 9),

        # Alternating pattern, still majority
        ([1, 2, 1, 2, 1, 2, 1], 1),

        # Large group of same numbers
        ([4] * 100 + [3] * 49, 4),

        # Mixed random values but with a clear majority
        ([10, 1, 10, 2, 10, 3, 10, 4, 10, 10, 10], 10),

        # Majority element is negative
        ([-1, -1, -1, 2, 3, -1, 4], -1),

        # Multiple numbers but still one majority
        ([5, 1, 5, 2, 5, 3, 5, 4, 5], 5),

        # All same elements
        ([8, 8, 8, 8, 8], 8),

        # Large test (for stress testing performance)
        ([9] * 5000 + [8] * 4999, 9)
    ]

    sol = Solution()

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = sol.majorityElement(nums)
        status = "✅ PASS" if result == expected else f"❌ FAIL (expected {expected})"
        print(f"Test {i:02}: Input (len={len(nums)}): {nums[:10]}{'...' if len(nums) > 10 else ''}")
        print(f" → Majority element: {result}  {status}\n")

    # Optional: allow user input
    user_input = input("Enter numbers separated by spaces (or press Enter to exit): ").strip()
    if user_input:
        nums = [int(x) for x in user_input.split()]
        print(f"Majority element: {sol.majorityElement(nums)}")


if __name__ == "__main__":
    main()