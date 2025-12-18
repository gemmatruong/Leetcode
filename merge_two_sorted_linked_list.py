from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # WAY 1: Long version
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head = list1
            current1 = list1.next
            current2 = list2
        else:
            head = list2
            current1 = list1
            current2 = list2.next
        
        node = head
        while (current1 or current2):
            if current1 == None:
                node.next = current2
                node = node.next
                current2 = current2.next

            elif current2 == None:
                node.next = current1
                node = node.next
                current1 = current1.next

            else:
                if current1.val <= current2.val:
                    node.next = current1
                    node = node.next
                    current1 = current1.next
                else:
                    node.next = current2
                    node = node.next
                    current2 = current2.next
        return head



def main():
    sol = Solution()

    # Helper: build linked list from Python list
    def build_list(arr):
        dummy = ListNode()
        cur = dummy
        for v in arr:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    # Helper: convert linked list to Python list
    def to_list(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    print("TEST CASES FOR mergeTwoLists:")

    # 1. Both lists empty
    l1 = None
    l2 = None
    print(to_list(sol.mergeTwoLists(l1, l2)))   # []

    # 2. First list empty
    l1 = None
    l2 = build_list([1, 3, 5])
    print(to_list(sol.mergeTwoLists(l1, l2)))   # [1,3,5]

    # 3. Second list empty
    l1 = build_list([2, 4, 6])
    l2 = None
    print(to_list(sol.mergeTwoLists(l1, l2)))   # [2,4,6]

    # 4. Both lists single element
    l1 = build_list([1])
    l2 = build_list([2])
    print(to_list(sol.mergeTwoLists(l1, l2)))   # [1,2]

    # 5. Interleaving values
    l1 = build_list([1, 3, 5])
    l2 = build_list([2, 4, 6])
    print(to_list(sol.mergeTwoLists(l1, l2)))   # [1,2,3,4,5,6]

    # 6. One list entirely smaller
    l1 = build_list([1, 2, 3])
    l2 = build_list([4, 5, 6])
    print(to_list(sol.mergeTwoLists(l1, l2)))   # [1,2,3,4,5,6]

    # 7. Duplicate values
    l1 = build_list([1, 2, 2, 4])
    l2 = build_list([1, 2, 3])
    print(to_list(sol.mergeTwoLists(l1, l2)))   # [1,1,2,2,2,3,4]

    # 8. Negative numbers
    l1 = build_list([-3, -1, 2])
    l2 = build_list([-2, 0, 3])
    print(to_list(sol.mergeTwoLists(l1, l2)))   # [-3,-2,-1,0,2,3]

    # 9. Lists of different lengths
    l1 = build_list([1, 4, 7, 8, 9])
    l2 = build_list([2, 3])
    print(to_list(sol.mergeTwoLists(l1, l2)))   # [1,2,3,4,7,8,9]

    # 10. Larger lists
    l1 = build_list([1, 3, 5, 7, 9])
    l2 = build_list([0, 2, 4, 6, 8, 10])
    print(to_list(sol.mergeTwoLists(l1, l2)))   # [0,1,2,3,4,5,6,7,8,9,10]


if __name__ == "__main__":
    main()
