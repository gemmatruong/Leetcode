from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Use DFS
        # if not root:
        #     return []
        # result = [root.val]
        
        # def dfs(l, r):
        #     if not l and not r:
        #         return
        #     if l:
        #         result.append(l.val)
        #         dfs(l.left, l.right)
        #     if r:
        #         result.append(r.val)
        #         dfs(r.left, r.right)
        # dfs(root.left, root.right)
        # return result
        
        # Cleaner way: also using DFS iterative
        # result = []
        # def dfs(node):
        #     if not node:
        #         return
        #     result.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return result
        
        # Way 3: DFS using stack
        if not root:
            return []
        result = []
        stack = [root]  # LIFO

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

def main():
    sol = Solution()

    # Helper to create nodes quickly
    def node(val, left=None, right=None):
        return TreeNode(val, left, right)

    print("TEST CASES FOR preorderTraversal:")

    # 1. Empty tree
    root1 = None
    print(sol.preorderTraversal(root1))
    # Expected: []

    # 2. Single node
    root2 = node(1)
    print(sol.preorderTraversal(root2))
    # Expected: [1]

    # 3. Two-level full tree
    #       1
    #     /   \
    #    2     3
    root3 = node(1, node(2), node(3))
    print(sol.preorderTraversal(root3))
    # Expected: [1, 2, 3]

    # 4. Left-skewed tree
    # 1 -> 2 -> 3 -> 4
    root4 = node(1, node(2, node(3, node(4))))
    print(sol.preorderTraversal(root4))
    # Expected: [1, 2, 3, 4]

    # 5. Right-skewed tree
    # 1 -> 2 -> 3 -> 4 (right side)
    root5 = node(1, None, node(2, None, node(3, None, node(4))))
    print(sol.preorderTraversal(root5))
    # Expected: [1, 2, 3, 4]

    # 6. Mixed tree
    #       1
    #      / \
    #     2   3
    #      \
    #       5
    root6 = node(1,
                 node(2, None, node(5)),
                 node(3))
    print(sol.preorderTraversal(root6))
    # Expected: [1, 2, 5, 3]

    # 7. Larger full tree
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7
    root7 = node(1,
                 node(2, node(4), node(5)),
                 node(3, node(6), node(7)))
    print(sol.preorderTraversal(root7))
    # Expected: [1, 2, 4, 5, 3, 6, 7]

    # 8. Tree with negative values
    #       1
    #      / \
    #    -2   3
    root8 = node(1, node(-2), node(3))
    print(sol.preorderTraversal(root8))
    # Expected: [1, -2, 3]

    # 9. Tree with duplicate values
    #        1
    #       / \
    #      1   1
    root9 = node(1, node(1), node(1))
    print(sol.preorderTraversal(root9))
    # Expected: [1, 1, 1]

    # 10. More complex tree
    #         1
    #       /   \
    #      2     3
    #     / \     \
    #    4   5     6
    #       /
    #      7
    root10 = node(1,
                  node(2, node(4), node(5, node(7))),
                  node(3, None, node(6)))
    print(sol.preorderTraversal(root10))
    # Expected: [1, 2, 4, 5, 7, 3, 6]

main()
