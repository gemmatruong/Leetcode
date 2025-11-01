from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # for num in nums:
        #     if nums.count(num) == 1:
        #         return num
        
        # Using XOR operation: ^
        num = 0
        for n in nums:
            num ^= n
        
        return num

def main():
    test_cases = [
        [2, 2, 1],                  # single number = 1
        [4, 1, 2, 1, 2],            # single number = 4
        [1],                        # single number = 1
        [0, 0, 7],                  # single number = 7
        [9, 9, 8, 8, 3],            # single number = 3
        [10, 11, 10],               # single number = 11
        [5, 5, 6, 7, 7],            # single number = 6
        [100, 200, 100],            # single number = 200
        [-1, -1, -5, -2, -2],       # single number = -5
        [3, 3, 4, 3, 3],            # single number = 4
    ]

    sol = Solution()

    for i, nums in enumerate(test_cases, start=1):
        print(f"Test Case {i}: {nums}")
        print(f"→ Single Number: {sol.singleNumber(nums)}\n")


if __name__ == "__main__":
    main()