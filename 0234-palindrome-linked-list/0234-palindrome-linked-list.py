# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverseLL(curr):
            reverse = None
            while curr:
                temp = ListNode(curr.val)
                curr= curr.next
                temp.next = reverse
                reverse = temp
            return reverse
        curr = head
        rev = reverseLL(curr)
        while rev and head:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True
