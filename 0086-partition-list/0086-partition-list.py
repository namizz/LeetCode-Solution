# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        start = ListNode("None")
        s1 = start
        end = ListNode("None")
        s2 = end
        curr = head
        while curr:
            if curr.val < x:
                start.next = curr
                start = start.next 
            else:
                end.next = curr
                end = end.next

            curr = curr.next
        start.next = s2.next
        end.next = None
        return s1.next

                
        