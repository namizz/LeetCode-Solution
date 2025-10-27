# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode("None")
        dummy.next = head
        curr = head
        prev = dummy
        while curr and curr.next:
            a = curr
            b = curr.next
            if prev:
                prev.next = b
                # update prev
            curr.next = b.next
            b.next = a
            prev = a
            curr = curr.next
        return dummy.next
            


        