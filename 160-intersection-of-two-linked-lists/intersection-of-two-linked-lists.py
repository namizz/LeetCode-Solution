# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nA, nB = 1,1
        listA = headA
        listB = headB
        while listA.next:
            listA = listA.next
            nA += 1
        while listB.next:
            listB = listB.next
            nB += 1
        listA = headA
        listB = headB
        if nA < nB:
            while nA != nB:
                listB = listB.next
                nB -= 1
        elif nA > nB:
            while nA != nB:
                listA = listA.next
                nA -= 1
        while listA != listB:
            listA = listA.next
            listB = listB.next
        return listA
        
        
        