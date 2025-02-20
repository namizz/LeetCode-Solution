# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        r = head
        
        while r and r.next:
            t = t.next
            r = r.next.next

            if t == r:
                break
        if not (r and r.next):
            return None
        
        t = head
        while r and t != r:
            t = t.next
            r = r.next
        return r
            

        
        