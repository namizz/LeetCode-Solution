# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force
        # using bubble sort, sort from last to first
        # make it effeicient by
        # merge sort
        # find the length of linked list
        # find give to right the right half and give to left the left half
        # 3 | 1 2
        def merge(left, right):
            dummy = ListNode("None")
            curr = dummy
            while left and right:
                if left.val < right.val:
                    curr.next = left                    
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next

            curr.next = left or right
            return dummy.next

        def mid(ll):
            slow, fast = ll, ll.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        
        def merge_sort(ll):
            if not ll or not ll.next:
                return ll if ll else None
            center = mid(ll)
            rr = center.next
            center.next = None
   
            left = merge_sort(ll)
            right = merge_sort(rr)

            return merge(left,right)
        return merge_sort(head)



        