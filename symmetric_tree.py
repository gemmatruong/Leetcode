# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSame(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return isSame(left.left, right.right) and isSame(left.right, right.left)

        return isSame(root.left, root.right)

# --------------------------------------------
# MAIN FUNCTION WITH 10 TEST CASES FOR SYMMETRY
# --------------------------------------------

def main():
    sol = Solution()

    # Test Case 1: empty tree → True
    print("TC1:", sol.isSymmetric(None))

    # Test Case 2: single node → True
    t2 = TreeNode(1)
    print("TC2:", sol.isSymmetric(t2))

    # Test Case 3: simple symmetric tree
    t3 = TreeNode(1, TreeNode(2), TreeNode(2))
    print("TC3:", sol.isSymmetric(t3))

    # Test Case 4: asymmetric (missing child)
    t4 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2))
    print("TC4:", sol.isSymmetric(t4))

    # Test Case 5: symmetric structure but different values → False
    t5 = TreeNode(1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(2, TreeNode(4), TreeNode(99)))   # 3 ↔ 4 match, but 4 ↔ 99 mismatch
    print("TC5:", sol.isSymmetric(t5))

    # Test Case 6: deeper symmetric tree → True
    t6 = TreeNode(1,
            TreeNode(2,
                TreeNode(3),
                TreeNode(4)),
            TreeNode(2,
                TreeNode(4),
                TreeNode(3)))
    print("TC6:", sol.isSymmetric(t6))

    # Test Case 7: deeper asymmetric tree (one inner mismatch)
    t7 = TreeNode(1,
            TreeNode(2,
                TreeNode(3),
                TreeNode(5)),
            TreeNode(2,
                TreeNode(4),
                TreeNode(3)))
    print("TC7:", sol.isSymmetric(t7))

    # Test Case 8: left-heavy only → False
    t8 = TreeNode(1, TreeNode(2, TreeNode(3)), None)
    print("TC8:", sol.isSymmetric(t8))

    # Test Case 9: right-heavy only → False
    t9 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    print("TC9:", sol.isSymmetric(t9))

    # Test Case 10: symmetric with repeated values → True
    t10 = TreeNode(1,
            TreeNode(2,
                TreeNode(3),
                TreeNode(3)),
            TreeNode(2,
                TreeNode(3),
                TreeNode(3)))
    print("TC10:", sol.isSymmetric(t10))


if __name__ == "__main__":
    main()