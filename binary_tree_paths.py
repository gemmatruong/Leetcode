from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        

        # Way 2:
        path = []

        def dfs(node, current):
            if not node:
                return
            if current == "":
                current = str(node.val)
            else:
                current = current + "->" + str(node.val)
            
            if not node.left and not node.right:
                path.append(current)
            
            if node.left:
                dfs(node.left, current)
            if node.right:
                dfs(node.right, current)
        dfs(root, "")
        return path

def main():
    sol = Solution()

    # helper to shorten node creation
    def node(val, left=None, right=None):
        return TreeNode(val, left, right)

    print("TEST CASES FOR binaryTreePaths:")

    # 1. Empty tree
    root1 = None
    print(sol.binaryTreePaths(root1))
    # Expected: []

    # 2. Single node
    root2 = node(1)
    print(sol.binaryTreePaths(root2))
    # Expected: ["1"]

    # 3. Two-level full tree
    #       1
    #     /   \
    #    2     3
    root3 = node(1, node(2), node(3))
    print(sol.binaryTreePaths(root3))
    # Expected: ["1->2", "1->3"]

    # 4. Left-skewed tree
    # 1 -> 2 -> 3 -> 4
    root4 = node(1, node(2, node(3, node(4))))
    print(sol.binaryTreePaths(root4))
    # Expected: ["1->2->3->4"]

    # 5. Right-skewed tree
    # 1 -> 2 -> 3 -> 4 (right side)
    root5 = node(1, None, node(2, None, node(3, None, node(4))))
    print(sol.binaryTreePaths(root5))
    # Expected: ["1->2->3->4"]

    # 6. Mixed tree
    #       1
    #      / \
    #     2   3
    #      \
    #       5
    root6 = node(1,
                 node(2, None, node(5)),
                 node(3))
    print(sol.binaryTreePaths(root6))
    # Expected: ["1->2->5", "1->3"]

    # 7. Larger tree with multiple leaves
    #        1
    #       / \
    #      2   3
    #     /   / \
    #    4   5   6
    root7 = node(1,
                 node(2, node(4)),
                 node(3, node(5), node(6)))
    print(sol.binaryTreePaths(root7))
    # Expected: ["1->2->4", "1->3->5", "1->3->6"]

    # 8. Tree with single-leaf deep
    #        1
    #       /
    #      2
    #     /
    #    3
    #     \
    #      4
    root8 = node(1, node(2, node(3, None, node(4))))
    print(sol.binaryTreePaths(root8))
    # Expected: ["1->2->3->4"]

    # 9. Tree containing negative numbers
    #       1
    #      / \
    #    -2   3
    #        /
    #      -4
    root9 = node(1,
                 node(-2),
                 node(3, node(-4)))
    print(sol.binaryTreePaths(root9))
    # Expected: ["1->-2", "1->3->-4"]

    # 10. More complex branching
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
    print(sol.binaryTreePaths(root10))
    # Expected: ["1->2->4", "1->2->5->7", "1->3->6"]

main()
