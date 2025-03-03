# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = []
        dummy = ListNode("None")
        dummy.next = head
        slow = dummy.next
        fast = dummy.next
        while fast and fast.next:
            ans.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        i = len(ans)- 1 
        while slow:
            ans[i] += slow.val
            slow = slow.next
            i -= 1
        return max(ans)

        