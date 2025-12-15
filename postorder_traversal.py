from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # WAY 1: Use stack
        # if not root:
        #     return []
        # stack = [root]
        # result = []
        
        # while stack:
        #     node = stack.pop()
        #     result.append(node.val)

        #     for i in range(len(node.children)):
        #         stack.append(node.children[i])
        # return result[::-1]

        # WAY 2: use recursion
        if not root:
            return []

        result = []

        if root.children:
            for child in root.children:
                result += self.postorder(child)
        
        result.append(root.val)
        return result


def main():
    sol = Solution()

    # Helper to create nodes easily
    def node(val, children=None):
        return Node(val, children or [])

    print("TEST CASES FOR N-ARY TREE POSTORDER:")

    # 1. Empty tree
    root1 = None
    print(sol.postorder(root1))   # []

    # 2. Single node
    root2 = node(1)
    print(sol.postorder(root2))   # [1]

    # 3. Root with multiple children
    #      1
    #   /  |  \
    #  2   3   4
    root3 = node(1, [node(2), node(3), node(4)])
    print(sol.postorder(root3))   # [2,3,4,1]

    # 4. Two-level tree
    #        1
    #      /   \
    #     2     3
    #          |
    #          4
    root4 = node(1, [
        node(2),
        node(3, [node(4)])
    ])
    print(sol.postorder(root4))   # [2,4,3,1]

    # 5. Deep single branch
    # 1 -> 2 -> 3 -> 4
    root5 = node(1, [node(2, [node(3, [node(4)])])])
    print(sol.postorder(root5))   # [4,3,2,1]

    # 6. Mixed branching
    #         1
    #     /   |    \
    #    2    3     4
    #        / \
    #       5   6
    root6 = node(1, [
        node(2),
        node(3, [node(5), node(6)]),
        node(4)
    ])
    print(sol.postorder(root6))   # [2,5,6,3,4,1]

    # 7. Tree with negative values
    #        1
    #      /   \
    #    -2    -3
    root7 = node(1, [node(-2), node(-3)])
    print(sol.postorder(root7))   # [-2,-3,1]

    # 8. Tree with duplicate values
    #        1
    #      /   \
    #     1     1
    root8 = node(1, [node(1), node(1)])
    print(sol.postorder(root8))   # [1,1,1]

    # 9. Larger tree
    #          1
    #       /  |  \
    #      2   3   4
    #         / \
    #        5   6
    #           |
    #           7
    root9 = node(1, [
        node(2),
        node(3, [node(5), node(6, [node(7)])]),
        node(4)
    ])
    print(sol.postorder(root9))   # [2,5,7,6,3,4,1]

    # 10. Wide tree (many children)
    #      1
    #  / / / / / 
    # 2 3 4 5 6
    root10 = node(1, [node(2), node(3), node(4), node(5), node(6)])
    print(sol.postorder(root10))  # [2,3,4,5,6,1]


if __name__ == "__main__":
    main()
