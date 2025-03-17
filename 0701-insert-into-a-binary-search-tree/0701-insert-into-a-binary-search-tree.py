# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        dummy = root
        while dummy:
            if dummy.val > val:
                if not dummy.left:
                    dummy.left = TreeNode(val)
                    break
                dummy = dummy.left
            else:
                if not dummy.right:
                    dummy.right = TreeNode(val)
                    break
                dummy = dummy.right
        return root
        
        