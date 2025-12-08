from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # WAY 1: use DFS
        # # If it is empty node, return False
        # if not root:
        #     return False
        
        # # If it is the leaf, return true if match the target, otherwise return false
        # if not root.left and not root.right:
        #     return targetSum == root.val
        
        # # This statement will make sure we check both left branch and right branch
        # # We only need 1 matched branch, OR function will make sure just 1 True will return True
        # # Ex: False or True --> return True
        # return (self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val))

        # Way 2: Use BFS
        if not root:
            return False
        
        # FIFO data structure
        queue = deque()
        # Add a list of two element (the node and its value) to the queue
        queue.append([root, root.val])

        while queue:
            # Take the front node in the queue
            node, current_sum = queue.popleft()
            
            # check if it is the leaf node, return True if the sums match
            if not node.left and not node.right and current_sum == targetSum:
                return True
            
            # If it not the leaf
            # and it has left child, append left child
            if node.left:
                queue.append([node.left, current_sum + node.left.val])
            # and it has right child, append right child
            if node.right:
                queue.append([node.right, current_sum + node.right.val])
        return False

def main():
    sol = Solution()
    tests = []

    # Test 1: Simple true path
    root1 = TreeNode(5, TreeNode(4), TreeNode(8))
    tests.append((root1, 9))   # 5 → 4

    # Test 2: Simple false path
    tests.append((root1, 20))

    # Test 3: LeetCode classic tree (true)
    root2 = TreeNode(5,
                TreeNode(4,
                    TreeNode(11, TreeNode(7), TreeNode(2))),
                TreeNode(8,
                    TreeNode(13),
                    TreeNode(4, None, TreeNode(1))))
    tests.append((root2, 22))  # valid: 5 → 4 → 11 → 2

    # Test 4: Same tree, false case
    tests.append((root2, 26))

    # Test 5: Single-node tree, true
    root3 = TreeNode(7)
    tests.append((root3, 7))

    # Test 6: Single-node tree, false
    tests.append((root3, 10))

    # Test 7: Empty tree
    tests.append((None, 5))

    # Test 8: Tree with negative numbers (true)
    root4 = TreeNode(1,
                TreeNode(-2,
                    TreeNode(1, TreeNode(-1)),
                    TreeNode(3)),
                TreeNode(-3, TreeNode(-2)))
    tests.append((root4, -1))  # 1 → -2 → 1 → -1

    # Test 9: Tree with negative numbers (false)
    tests.append((root4, -5))

    # Test 10: Larger balanced tree (true)
    root5 = TreeNode(1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, TreeNode(6), TreeNode(7)))
    tests.append((root5, 11))  # 1 → 3 → 7

    # Run Tests
    for i, (root, target) in enumerate(tests, 1):
        result = sol.hasPathSum(root, target)
        print(f"Test {i}: target={target}, result={result}")

main()