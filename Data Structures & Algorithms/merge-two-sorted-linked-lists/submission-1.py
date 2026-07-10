# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        if not l1 and not l2:
            return None

        if not l1 and l2:
            return l2
        
        if not l2 and l1:
            return l1
        
        if l1.val > l2.val:
            x = ListNode(l2.val)
            l2 = l2.next
        else:
            x = ListNode(l1.val)
            l1 = l1.next

        ans = x

        while l1 and l2:
            if l1.val > l2.val:
                x.next = ListNode(l2.val)
                l2 = l2.next
            else:
                x.next = ListNode(l1.val)
                l1 = l1.next
            x = x.next

        if l1:
            x.next = l1
        if l2:
            x.next = l2

        return ans
