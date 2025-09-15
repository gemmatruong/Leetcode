import sys
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            i = 0
            for j in range(1, len(nums)):
                if nums[i] != nums[j]:
                    nums[i+1] = nums[j]
                    i += 1
            return i+1

def main():
    nums1 = [1,1,2]; # Input array
    nums2 = [0,0,1,1,1,2,2,3,3,4] # Input array
    expectedNums1 = [1,2] #The expected answer with correct length
    expectedNums2 = [0,1,2,3,4] #The expected answer with correct length

    sol = Solution()
    k1 = sol.removeDuplicates(nums1) # Calls your implementation
    k2 = sol.removeDuplicates(nums2) # Calls your implementation

    assert k1 == len(expectedNums1)
    for i in range(k1):
        assert nums1[i] == expectedNums1[i]
    
    print(k1, nums1[:k1])
    
    assert k2 == len(expectedNums2)
    for i in range(k2):
        assert nums2[i] == expectedNums2[i]
    
    print(k2, nums2[:k2])
    
    print("\nAll tests passed.")

if __name__ == "__main__":
    main()
