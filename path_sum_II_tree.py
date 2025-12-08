from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Way 1: Use BFS
        if not root:
            return []

        queue = deque()
        # A queue with each element including a node, current sum, and a current path
        queue.append([root, root.val, [root.val]])
        result = []

        while queue:
            # get the front element from queue
            node, current_sum, path = queue.popleft()

            # if it is a leaf and sums equal, add the current path to result list
            if not node.left and not node.right and current_sum == targetSum:
                result.append(path)
            
            if node.left:
                queue.append([node.left, current_sum + node.left.val, path + [node.left.val]])
            if node.right:
                queue.append([node.right, current_sum + node.right.val, path + [node.right.val]])
        return result

        # WAY 2: Use DFS
        # result = []     # A list of result path
        # path = []       # A list keep track of current path
        
        # # target is the remaining sum, we decrease it by node's value every time travel to a new node
        # def dfs(node, target):  
        #     if not node:
        #         return

        #     # Add new node's value to current path
        #     path.append(node.val)

        #     # If node is a leaf and remaining sum equals the node's value, 
        #     # add the current path to result list
        #     # use list() function to add a copy of the current path instead of its address.
        #     if not node.left and not node.right and node.val == target:
        #         result.append(list(path))

        #     # traverse thru the left branch, decrease the remaining sum by the node's value
        #     dfs(node.left, target - node.val)
        #     # traverse thru the right branch, decrease the remaining sum by the node's value
        #     dfs(node.right, target - node.val)
            
        #     # remove the node has been checked both left and right children from the current path
        #     path.pop()

        # dfs(root, targetSum)       
        # return result

def main():
    sol = Solution()

    # Helper function
    def node(val, left=None, right=None):
        return TreeNode(val, left, right)

    print("TEST CASES FOR pathSum:")

    # 1. Empty tree
    root1 = None
    print(sol.pathSum(root1, 5))  
    # Expected: []

    # 2. Single node matching
    root2 = node(7)
    print(sol.pathSum(root2, 7))  
    # Expected: [[7]]

    # 3. Single node not matching
    root3 = node(3)
    print(sol.pathSum(root3, 5))  
    # Expected: []

    # 4. Two-level tree with one valid path
    #       5
    #      / \
    #     4   8
    root4 = node(5, node(4), node(8))
    print(sol.pathSum(root4, 9))  
    # Expected: [[5,4]]

    # 5. Example from LeetCode
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \      \
    # 7    2      1
    root5 = node(5,
                 node(4, node(11, node(7), node(2))),
                 node(8, node(13), node(4, None, node(1))))
    print(sol.pathSum(root5, 22))
    # Expected: [[5,4,11,2]]

    # 6. Tree with multiple valid paths
    #        1
    #       / \
    #      2   3
    #     /   / \
    #    4   2   1
    root6 = node(1,
                 node(2, node(4)),
                 node(3, node(2), node(1)))
    print(sol.pathSum(root6, 7))
    # Expected: [[1,2,4], [1,3,2], [1,3,1,2]? No, leaf only → [[1,2,4], [1,3,2]]

    # 7. Negative values
    #         1
    #        / \
    #      -2   -3
    #     / \     \
    #    1   3     -2
    root7 = node(1,
                 node(-2, node(1), node(3)),
                 node(-3, None, node(-2)))
    print(sol.pathSum(root7, -1))
    # Expected: [[1, -2, 1], [1, -3, -2]]

    # 8. No path reaches target
    root8 = node(1,
                 node(2),
                 node(3))
    print(sol.pathSum(root8, 100))
    # Expected: []

    # 9. Large tree with multiple branches
    #        10
    #       /  \
    #      5    12
    #     / \     \
    #    4   7     2
    root9 = node(10,
                 node(5, node(4), node(7)),
                 node(12, None, node(2)))
    print(sol.pathSum(root9, 19))
    # Expected: [[10,5,4], [10,12,-3]? No → Only [[10,5,4]]

    # 10. Complex tree with multiple valid paths
    #           5
    #         /   \
    #        3     6
    #       / \   / \
    #      2   1 4   3
    root10 = node(5,
                  node(3, node(2), node(1)),
                  node(6, node(4), node(3)))
    print(sol.pathSum(root10, 10))
    # Expected: [[5,3,2], [5,6,-1]? No → [[5,3,2], [5,6,4] is NOT leaf → only [[5,3,2]]

main()