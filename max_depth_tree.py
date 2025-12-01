# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # WAY 1: count left branch and right brand --> get the bigger count
        # if not root:
        #     return 0
        # l_count = self.maxDepth(root.left)
        # r_count = self.maxDepth(root.right)
        
        # return 1 + max(l_count, r_count)

        # WAY 2: faster way. Use a helper function to count
        def count(node):
            if not node:
                return 0
            return 1 + max(count(node.left), count(node.right))
        return count(root)

# --------------------------------------------
# MAIN FUNCTION WITH 10 TEST CASES
# --------------------------------------------

def main():
    sol = Solution()

    # Test Case 1: empty tree → depth 0
    print("TC1:", sol.maxDepth(None))

    # Test Case 2: single node → depth 1
    t2 = TreeNode(1)
    print("TC2:", sol.maxDepth(t2))

    # Test Case 3: root + left child → depth 2
    t3 = TreeNode(1, TreeNode(2), None)
    print("TC3:", sol.maxDepth(t3))

    # Test Case 4: root + right child → depth 2
    t4 = TreeNode(1, None, TreeNode(3))
    print("TC4:", sol.maxDepth(t4))

    # Test Case 5: balanced tree of depth 3
    t5 = TreeNode(1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)))
    print("TC5:", sol.maxDepth(t5))

    # Test Case 6: left-skewed tree (depth = 4)
    t6 = TreeNode(1,
            TreeNode(2,
                TreeNode(3,
                    TreeNode(4))))
    print("TC6:", sol.maxDepth(t6))

    # Test Case 7: right-skewed tree (depth = 5)
    t7 = TreeNode(1,
            None,
            TreeNode(2,
                None,
                TreeNode(3,
                    None,
                    TreeNode(4,
                        None,
                        TreeNode(5)))))
    print("TC7:", sol.maxDepth(t7))

    # Test Case 8: unbalanced tree (left deeper)
    t8 = TreeNode(1,
            TreeNode(2,
                TreeNode(3)),
            TreeNode(4))
    print("TC8:", sol.maxDepth(t8))  # expected depth = 3

    # Test Case 9: unbalanced tree (right deeper)
    t9 = TreeNode(1,
            TreeNode(2),
            TreeNode(3,
                None,
                TreeNode(5,
                    None,
                    TreeNode(7))))
    print("TC9:", sol.maxDepth(t9))  # expected depth = 4

    # Test Case 10: complex mix (depth = 4)
    t10 = TreeNode(1,
             TreeNode(2,
                 TreeNode(4),
                 None),
             TreeNode(3,
                 TreeNode(5,
                     TreeNode(7)),
                 None))
    print("TC10:", sol.maxDepth(t10))  # expected depth = 4


if __name__ == "__main__":
    main()