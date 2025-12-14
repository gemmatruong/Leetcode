from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # WAY 1: use dfs traversing right to left, adding top to bottom, then reverse the list
        # result = []
        # def dfs(node):
        #     if not node:
        #         return
        #     result.append(node.val)
        #     if node.right:
        #         dfs(node.right)
        #     if node.left:
        #         dfs(node.left)
        # dfs(root)
        # result.reverse()
        # return result

        # WAY 2: use dfs traversing left to right, adding bottom to top
        # result = []
        # def dfs(node):
        #     if not node:
        #         return
        #     if node.left:
        #         dfs(node.left)
        #     if node.right:
        #         dfs(node.right)
        #     result.append(node.val)
        # dfs(root)
        # return result

        # WAY 3: use stack
        if not root:
            return []
            
        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        result.reverse()
        return result

def main():
    sol = Solution()

    def node(val, left=None, right=None):
        return TreeNode(val, left, right)

    print("TEST CASES FOR postorderTraversal:")

    # 1. Empty tree
    root1 = None
    print(sol.postorderTraversal(root1))   # []

    # 2. Single node
    root2 = node(1)
    print(sol.postorderTraversal(root2))   # [1]

    # 3. Two-level tree
    #     1
    #    / \
    #   2   3
    root3 = node(1, node(2), node(3))
    print(sol.postorderTraversal(root3))   # [2, 3, 1]

    # 4. Left-skewed tree
    # 1 -> 2 -> 3 -> 4
    root4 = node(1, node(2, node(3, node(4))))
    print(sol.postorderTraversal(root4))   # [4, 3, 2, 1]

    # 5. Right-skewed tree
    # 1 -> 2 -> 3 -> 4
    root5 = node(1, None, node(2, None, node(3, None, node(4))))
    print(sol.postorderTraversal(root5))   # [4, 3, 2, 1]

    # 6. Mixed tree
    #     1
    #    / \
    #   2   3
    #    \
    #     5
    root6 = node(1, node(2, None, node(5)), node(3))
    print(sol.postorderTraversal(root6))   # [5, 2, 3, 1]

    # 7. Full binary tree
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   7
    root7 = node(1,
                 node(2, node(4), node(5)),
                 node(3, node(6), node(7)))
    print(sol.postorderTraversal(root7))   # [4,5,2,6,7,3,1]

    # 8. Tree with negative values
    #     1
    #    / \
    #  -2   3
    root8 = node(1, node(-2), node(3))
    print(sol.postorderTraversal(root8))   # [-2, 3, 1]

    # 9. Tree with duplicate values
    #     1
    #    / \
    #   1   1
    root9 = node(1, node(1), node(1))
    print(sol.postorderTraversal(root9))   # [1,1,1]

    # 10. Complex tree
    #        1
    #      /   \
    #     2     3
    #    / \     \
    #   4   5     6
    #      /
    #     7
    root10 = node(1,
                  node(2, node(4), node(5, node(7))),
                  node(3, None, node(6)))
    print(sol.postorderTraversal(root10))  # [4,7,5,2,6,3,1]


if __name__ == "__main__":
    main()
