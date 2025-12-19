from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:


        # WAY 2: use two pointers. O(m+n) time and O(1) memory
        # A travels distance a + c + b
        # B travels distance b + c + a
        # A and B will meet at the intersection or the None (end of both lists)
        if not headA or not headB:
            return None

        pointerA = headA
        pointerB = headB

        while pointerA is not pointerB:
            if pointerA is None:
                pointerA = headB
            else:
                pointerA = pointerA.next
            
            if pointerB is None:
                pointerB = headA
            else:
                pointerB = pointerB.next

        return pointerA
        
        
def main():
    sol = Solution()

    # Helper: build linked list from list, return head
    def build_list(arr):
        dummy = ListNode(0)
        cur = dummy
        for v in arr:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    # Helper: get tail of a linked list
    def get_tail(head):
        while head and head.next:
            head = head.next
        return head

    # Helper: print intersection result
    def print_intersection(node):
        print(node.val if node else None)

    print("TEST CASES FOR getIntersectionNode:")

    # 1. Both lists empty
    headA = None
    headB = None
    print_intersection(sol.getIntersectionNode(headA, headB))  # None

    # 2. One list empty
    headA = build_list([1, 2, 3])
    headB = None
    print_intersection(sol.getIntersectionNode(headA, headB))  # None

    # 3. No intersection, same values
    headA = build_list([1, 2, 3])
    headB = build_list([1, 2, 3])
    print_intersection(sol.getIntersectionNode(headA, headB))  # None

    # 4. Intersection at last node
    common = build_list([8])
    headA = build_list([1, 2, 3])
    headB = build_list([4, 5])
    get_tail(headA).next = common
    get_tail(headB).next = common
    print_intersection(sol.getIntersectionNode(headA, headB))  # 8

    # 5. Intersection in the middle
    common = build_list([7, 8, 9])
    headA = build_list([1, 2, 3])
    headB = build_list([4, 5])
    get_tail(headA).next = common
    get_tail(headB).next = common
    print_intersection(sol.getIntersectionNode(headA, headB))  # 7

    # 6. One node intersection (entire list)
    common = build_list([1, 2, 3])
    headA = common
    headB = common
    print_intersection(sol.getIntersectionNode(headA, headB))  # 1

    # 7. Long A, short B, intersect near end
    common = build_list([6, 7])
    headA = build_list([1, 2, 3, 4, 5])
    headB = build_list([9])
    get_tail(headA).next = common
    get_tail(headB).next = common
    print_intersection(sol.getIntersectionNode(headA, headB))  # 6

    # 8. Short A, long B, intersect near start
    common = build_list([3, 4, 5])
    headA = build_list([1, 2])
    headB = build_list([9, 8, 7])
    get_tail(headA).next = common
    get_tail(headB).next = common
    print_intersection(sol.getIntersectionNode(headA, headB))  # 3

    # 9. No intersection, different lengths
    headA = build_list([1, 2, 3, 4])
    headB = build_list([5, 6])
    print_intersection(sol.getIntersectionNode(headA, headB))  # None

    # 10. Intersection at head of B
    common = build_list([10, 11])
    headA = build_list([1, 2, 3])
    headB = common
    get_tail(headA).next = common
    print_intersection(sol.getIntersectionNode(headA, headB))  # 10


if __name__ == "__main__":
    main()
