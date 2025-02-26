# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # head = l2
        # l2.val += l1.val + rem if l2.val > 10:
        # l2.val %10
        # rem = l2.val//10
        # if rem
        
        dummy = ListNode("None")
        curr = dummy
        rem = 0
        while l1 or l2:
            temp = ListNode(0)
            if l1:
                temp.val += l1.val
                l1 = l1.next
            if l2:
                temp.val += l2.val
                l2 = l2.next
            temp.val += rem
            added = temp.val 

            if added > 9:
                temp.val = added%10
                rem = added//10
            else:
                rem = 0
            curr.next = temp
            curr = curr.next


        if rem:
            curr.next = ListNode(rem)
        return dummy.next
            
