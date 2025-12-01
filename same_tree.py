# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:        
        # WAY 1: recursively check two nodes
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # WAY 2: pre-order traversal. Compare two lists
        # def visit(root):
        #     if root is None:
        #         return [None]
        #     return [root.val] + visit(root.left) + visit(root.right)
        # return visit(p) == visit(q)

# -------------------------------
# MAIN FUNCTION WITH 10 TEST CASES
# -------------------------------

def main():
    sol = Solution()

    # Test Case 1: both trees empty → True
    print("TC1:", sol.isSameTree(None, None))

    # Test Case 2: one empty, one not → False
    t2_p = TreeNode(1)
    print("TC2:", sol.isSameTree(t2_p, None))

    # Test Case 3: same single node tree → True
    t3_p = TreeNode(5)
    t3_q = TreeNode(5)
    print("TC3:", sol.isSameTree(t3_p, t3_q))

    # Test Case 4: different single node values → False
    t4_p = TreeNode(1)
    t4_q = TreeNode(2)
    print("TC4:", sol.isSameTree(t4_p, t4_q))

    # Test Case 5: identical small binary tree
    t5_p = TreeNode(1, TreeNode(2), TreeNode(3))
    t5_q = TreeNode(1, TreeNode(2), TreeNode(3))
    print("TC5:", sol.isSameTree(t5_p, t5_q))

    # Test Case 6: different structure (one missing left child)
    t6_p = TreeNode(1, None, TreeNode(3))
    t6_q = TreeNode(1, TreeNode(3), None)
    print("TC6:", sol.isSameTree(t6_p, t6_q))

    # Test Case 7: deeper identical trees → True
    t7_p = TreeNode(1,
                    TreeNode(2, TreeNode(4), TreeNode(5)),
                    TreeNode(3))
    t7_q = TreeNode(1,
                    TreeNode(2, TreeNode(4), TreeNode(5)),
                    TreeNode(3))
    print("TC7:", sol.isSameTree(t7_p, t7_q))

    # Test Case 8: identical structure but one value changed → False
    t8_p = TreeNode(1,
                    TreeNode(2, TreeNode(4), TreeNode(5)),
                    TreeNode(3))
    t8_q = TreeNode(1,
                    TreeNode(2, TreeNode(4), TreeNode(9)),  # 5 → 9
                    TreeNode(3))
    print("TC8:", sol.isSameTree(t8_p, t8_q))

    # Test Case 9: larger tree, different at deeper right child
    t9_p = TreeNode(10,
                    TreeNode(20, TreeNode(40), None),
                    TreeNode(30, None, TreeNode(60)))
    t9_q = TreeNode(10,
                    TreeNode(20, TreeNode(40), None),
                    TreeNode(30, None, TreeNode(99)))  # 60 → 99
    print("TC9:", sol.isSameTree(t9_p, t9_q))

    # Test Case 10: one tree is a subtree of the other → False
    t10_p = TreeNode(1, TreeNode(2, TreeNode(3)))
    t10_q = TreeNode(1, TreeNode(2))
    print("TC10:", sol.isSameTree(t10_p, t10_q))


if __name__ == "__main__":
    main()