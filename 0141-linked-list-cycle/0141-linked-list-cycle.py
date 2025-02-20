# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        r = head
        t = head
        while head and head.next:
            t = t.next
            r = r.next.next
            if not r:
                return False
            if t == r:
                return True
        return False

        