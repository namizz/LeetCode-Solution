# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val
             and mirror(left.left, right.right)
             and mirror(left.right, right.left))
        
        return mirror(root.left, root.right)


        