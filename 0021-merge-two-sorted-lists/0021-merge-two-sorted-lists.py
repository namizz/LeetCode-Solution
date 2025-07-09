# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode("None")
        curr = list3
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            else:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return list3.next

        