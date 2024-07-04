# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_c = 0
        list1 = head
        dummy = ListNode()
        while list1:
            list1 = list1.next
            node_c += 1
        middle = node_c//2
        i = 0
        list1 = head
        while i < middle:
            list1 = list1.next
            i += 1
        return list1

        