from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # Way 1
        if not root:
            return 0
        
        def dfs(node):
            if not node:
                return float('inf')
            if not node.left and not node.right:
                return 1
            return 1 + min(dfs(node.left), dfs(node.right))
        return dfs(root)
    
        # -------------------------------------
        # Way 2:
    #     if not root:
    #         return 0
        
    #     self.min_depth = float('inf')
    #     self.dfs(root, 0)
    #     return self.min_depth

    # def dfs(self, node, current_depth):
    #     if not node:
    #         return
    #     if not node.left and not node.right:
    #         self.min_depth = min(self.min_depth, current_depth+1)
    #     self.dfs(node.left, current_depth+1)
    #     self.dfs(node.right, current_depth+1)

        # Way 3: Using BFS
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        depth = 0

        while queue:
            depth += 1

            for _ in range(len(queue)):
                node = queue.popleft()
                
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth



def main():
    sol = Solution()

    # Helper function to simplify tree creation
    def node(val, left=None, right=None):
        return TreeNode(val, left, right)

    print("TEST CASES FOR minDepth:")

    # 1. Empty tree
    root1 = None
    print(sol.minDepth(root1))   # Expected: 0

    # 2. Single node tree
    root2 = node(1)
    print(sol.minDepth(root2))   # Expected: 1

    # 3. Two-level complete tree
    #       1
    #      / \
    #     2   3
    root3 = node(1, node(2), node(3))
    print(sol.minDepth(root3))   # Expected: 2

    # 4. Left-skewed tree
    #    1
    #   /
    #  2
    # /
    # 3
    root4 = node(1, node(2, node(3)))
    print(sol.minDepth(root4))   # Expected: 3

    # 5. Right-skewed tree
    # 1
    #  \
    #   2
    #    \
    #     3
    root5 = node(1, None, node(2, None, node(3)))
    print(sol.minDepth(root5))   # Expected: 3

    # 6. First leaf on left side
    #      1
    #     / \
    #    2   3
    #       /
    #      4
    root6 = node(1, node(2), node(3, node(4)))
    print(sol.minDepth(root6))   # Expected: 2

    # 7. First leaf deep on right
    #     1
    #    / 
    #   2   
    #    \
    #     3
    #      \
    #       4
    root7 = node(1, node(2, None, node(3, None, node(4))))
    print(sol.minDepth(root7))   # Expected: 2

    # 8. Mixed tree with a shallow leaf
    #        1
    #      /   \
    #     2     3
    #          / \
    #         4   5  <-- leaf, depth = 2
    root8 = node(1,
                 node(2),
                 node(3, node(4), node(5)))
    print(sol.minDepth(root8))   # Expected: 2

    # 9. Unbalanced but leaf on left
    #        1
    #      /  
    #     2   
    #    / \
    #   3   4  <-- leaf, depth = 3
    root9 = node(1, node(2, node(3), node(4)))
    print(sol.minDepth(root9))   # Expected: 3

    # 10. Larger tree with leaf deeper on one side
    #        1
    #       / \
    #      2   3
    #         / 
    #        4
    #       /
    #      5  <-- leaf, depth = 4
    root10 = node(1,
                  node(2),
                  node(3, node(4, node(5))))
    print(sol.minDepth(root10))   # Expected: 2 (because left child of root is leaf)

main()
