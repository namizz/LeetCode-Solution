# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = 0
        def value(root):
            nonlocal ans
            if not root:
                return None

            value(root.right)
            root.val += ans
            ans = root.val
            value(root.left)
            
            return root

        value(root)
        return root
        