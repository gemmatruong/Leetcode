from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # nums_dict = {}
        # for i in range(len(nums)):
        #     if nums[i] not in nums_dict:
        #         nums_dict[nums[i]] = [i]
        #     else:
        #         nums_dict[nums[i]].append(i)
        # print(nums_dict)
        # for v in nums_dict.values():
        #     if len(v) == 1:
        #         continue
        #     for j in range(1, len(v)):
        #         if abs(v[j]-v[j-1]) <= k:
        #             return True
        # return False
        # -------------------------------------------------------------
        # Use Sliding Window to solve:
        seen = {}
        for i, value in enumerate(nums):
            if value in seen and i - seen[value] <= k:
                return True
            seen[value] = i
        return False

def main():
    sol = Solution()

    tests = [
        # 1. Simple nearby duplicate
        ([1, 2, 3, 1], 3, True),

        # 2. Duplicate too far apart
        ([1, 0, 1, 1], 0, False),

        # 3. Adjacent duplicate (k = 1)
        ([1, 2, 3, 4, 4], 1, True),

        # 4. No duplicates at all
        ([1, 2, 3, 4], 2, False),

        # 5. Duplicates exist, but all too far apart
        ([1, 2, 3, 1, 2, 3], 1, False),

        # 6. Duplicate exactly k distance apart
        ([5, 6, 7, 5], 3, True),

        # 7. k larger than array length
        ([10, 20, 30, 10], 100, True),

        # 8. Multiple duplicates, one pair valid
        ([4, 5, 6, 4, 7, 4], 2, True),  # nearest pair: 3 & 5 = distance 3 > 2

        # 9. All elements same
        ([1, 1, 1, 1], 1, True),

        # 10. k = 0, never valid
        ([9, 7, 9], 0, False),
    ]

    for i, (nums, k, expected) in enumerate(tests, 1):
        print(f"\nTest {i}: nums={nums}, k={k}")
        result = sol.containsNearbyDuplicate(nums, k)
        print(f"Output:   {result}")
        print(f"Expected: {expected}")

if __name__ == "__main__":
    main()