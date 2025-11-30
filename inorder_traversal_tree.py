from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # O(logn)
        result = []
        def helper(node):
            if node:
                helper(node.left)
                result.append(node.val)
                helper(node.right)
        helper(root)
        return result

# Helper: build binary tree from level-order list
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        node = queue.pop(0)
        if node:
            if i < len(nodes):
                node.left = TreeNode(nodes[i]) if nodes[i] is not None else None
                queue.append(node.left)
            i += 1
            if i < len(nodes):
                node.right = TreeNode(nodes[i]) if nodes[i] is not None else None
                queue.append(node.right)
            i += 1
    return root


def main():
    sol = Solution()

    # 10 TEST CASES
    tests = [
        ([], []),                                      # 1. Empty tree
        ([1], [1]),                                    # 2. Single node
        ([1, 2, None], [2, 1]),                        # 3. Left child only
        ([1, None, 2], [1, 2]),                        # 4. Right child only
        ([1, 2, 3], [2, 1, 3]),                        # 5. Full small tree
        ([4, 3, None, 2, None, 1], [1, 2, 3, 4]),      # 6. Left-heavy
        ([1, None, 2, None, 3, None, 4], [1, 2, 3, 4]),# 7. Right-heavy
        ([4, 2, 6, 1, 3, None, 7], [1, 2, 3, 4, 6, 7]),# 8. Mixed tree
        ([5, 1, 7, None, 3, None, 9, 2], [1, 2, 3, 5, 7, 9]), # 9. Random shape
        ([2, 1, 2, None, None, None, 3], [1, 2, 2, 3]) # 10. Tree with duplicates
    ]

    for i, (tree_list, expected) in enumerate(tests, 1):
        root = build_tree(tree_list)
        result = sol.inorderTraversal(root)
        print(f"Test {i}: tree={tree_list}")
        print(f"Expected: {expected}")
        print(f"Got     : {result}")
        print("-" * 40)


# Run main
main()