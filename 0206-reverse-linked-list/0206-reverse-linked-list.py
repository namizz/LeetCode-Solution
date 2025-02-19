# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = None
        while head:
            temp = ListNode(head.val)
            head= head.next
            temp.next = reverse
            reverse = temp
        return reverse
        