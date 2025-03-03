# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int):
        ans = ListNode("None")
        a = ans
        dummy = ListNode("None")
        dummy.next = head
        curr = dummy.next
        lng = 0
        while curr:
            curr = curr.next
            lng += 1
        i = 0
        curr = dummy.next
        while i < lng//k:
            temp = list()
            x = k
            while x > 0 and curr:
                temp.append(curr.val)
                curr = curr.next
                x -= 1
            while temp:
                a.next = ListNode(temp.pop())
                a = a.next
            i += 1
        a.next = curr
        return ans.next
        