from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        # WAY 2: Use set()
        seen = set()

        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

def main():
    sol = Solution()

    # Helper to create linked list nodes
    def node(val):
        return ListNode(val)

    print("TEST CASES FOR hasCycle:")

    # 1. Empty list
    head1 = None
    print(sol.hasCycle(head1))   # Expected: False

    # 2. Single node, no cycle
    head2 = node(1)
    print(sol.hasCycle(head2))   # Expected: False

    # 3. Single node with cycle to itself
    head3 = node(1)
    head3.next = head3
    print(sol.hasCycle(head3))   # Expected: True

    # 4. Two nodes, no cycle
    head4 = node(1)
    head4.next = node(2)
    print(sol.hasCycle(head4))   # Expected: False

    # 5. Two nodes with cycle
    head5 = node(1)
    head5.next = node(2)
    head5.next.next = head5
    print(sol.hasCycle(head5))   # Expected: True

    # 6. Three nodes, cycle in the middle
    head6 = node(1)
    head6.next = node(2)
    head6.next.next = node(3)
    head6.next.next.next = head6.next
    print(sol.hasCycle(head6))   # Expected: True

    # 7. Three nodes, no cycle
    head7 = node(1)
    head7.next = node(2)
    head7.next.next = node(3)
    print(sol.hasCycle(head7))   # Expected: False

    # 8. Longer list, cycle at end
    head8 = node(1)
    head8.next = node(2)
    head8.next.next = node(3)
    head8.next.next.next = node(4)
    head8.next.next.next.next = head8.next
    print(sol.hasCycle(head8))   # Expected: True

    # 9. Longer list, cycle to head
    head9 = node(1)
    head9.next = node(2)
    head9.next.next = node(3)
    head9.next.next.next = node(4)
    head9.next.next.next.next = head9
    print(sol.hasCycle(head9))   # Expected: True

    # 10. Long list without cycle
    head10 = node(1)
    current = head10
    for i in range(2, 10):
        current.next = node(i)
        current = current.next
    print(sol.hasCycle(head10))  # Expected: False


if __name__ == "__main__":
    main()
