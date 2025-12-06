# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # WAY 1:
        # def check_height(node):
        #     if not node:
        #         return 0
            
        #     left = check_height(node.left)
        #     if left == -1:
        #         return -1
            
        #     right = check_height(node.right)
        #     if right == -1:
        #         return -1
            
        #     if abs(left-right) > 1:
        #         return -1
            
        #     return 1 + max(left, right)
        # return check_height(root) != -1

        # WAY 2
        def dfs(node):
            if not node:
                return [True, 0]
            left, right = dfs(node.left), dfs(node.right)
            balanced = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
       
        return dfs(root)[0]

def test_isBalanced():
    sol = Solution()

    # Helper to simplify tree creation
    def node(val, left=None, right=None):
        return TreeNode(val, left, right)

    # Test case 1: Empty tree
    root1 = None
    print(sol.isBalanced(root1))  # True

    # Test case 2: Single node
    root2 = node(1)
    print(sol.isBalanced(root2))  # True

    # Test case 3: Perfect tree
    root3 = node(1,
                 node(2, node(4), node(5)),
                 node(3, node(6), node(7)))
    print(sol.isBalanced(root3))  # True

    # Test case 4
    root4 = node(1,
                 node(2, node(4)),
                 node(3))
    print(sol.isBalanced(root4))  # True

    # Test case 5: Minimal unbalanced
    root5 = node(1,
                 node(2,
                      node(3)))
    print(sol.isBalanced(root5))  # False

    # Test case 6: Right-heavy unbalanced
    root6 = node(1, None,
                 node(2, None,
                      node(3)))
    print(sol.isBalanced(root6))  # False

    # Test case 7
    root7 = node(1,
                 node(2,
                      node(4,
                           node(5))),
                 node(3))
    print(sol.isBalanced(root7))  # False

    # Test case 8: Large balanced
    root8 = node(1,
                 node(2,
                      node(4),
                      node(5,
                           node(7),
                           node(8))),
                 node(3, None,
                      node(6)))
    print(sol.isBalanced(root8))  # True

    # Test case 9: Complex unbalanced
    root9 = node(1,
                 node(2,
                      node(4),
                      node(5,
                           node(6,
                                node(7)))),
                 node(3))
    print(sol.isBalanced(root9))  # False

    # Test case 10
    root10 = node(1,
                  node(2,
                       node(4),
                       node(5,
                            node(8))),
                  node(3,
                       node(6),
                       node(7)))
    print(sol.isBalanced(root10))  # True

if __name__ == "__main__":
    test_isBalanced()