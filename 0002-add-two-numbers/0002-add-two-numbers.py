# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode("None")
        curr = dummy
        r = 0
        while l1 and l2:
            k = l1.val + l2.val + r
            r = k//10
            k %= 10
            curr.next = ListNode(k)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            k = l1.val + r
            r = k//10
            k %= 10
            curr.next = ListNode(k)
            curr = curr.next
            l1 = l1.next
        while l2:
            k = l2.val + r
            r = k//10
            k %= 10
            curr.next = ListNode(k)
            curr = curr.next
            l2 = l2.next
        if r:
            curr.next = ListNode(r)
        return dummy.next
            

            


        