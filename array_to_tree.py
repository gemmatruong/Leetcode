from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # Time complexity: O(n); Space complexity: O(logn)
        def helper(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m-1)
            root.right = helper(m+1, r)
            return root

        return helper(0, len(nums) - 1)


# Helper function to print tree in level-order
def print_tree(root):
    if not root:
        print("[]")
        return
    q = deque([root])
    result = []
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    # Trim ending None values
    while result and result[-1] is None:
        result.pop()
    print(result)

def main():
    tests = [
        [],
        [1],
        [1,2],
        [1,2,3],
        [-5,-3,-1],
        [1,2,3,4],
        [-10,-3,0,5,9],
        [2,3,5,7,11,13],
        [1,3,4,6,8,10,13],
        [-20,-10,-3,0,2,4,6,11]
    ]

    sol = Solution()

    for i, nums in enumerate(tests, 1):
        print(f"Test Case {i}: {nums}")
        root = sol.sortedArrayToBST(nums)
        print_tree(root)
        print("-" * 40)

main()