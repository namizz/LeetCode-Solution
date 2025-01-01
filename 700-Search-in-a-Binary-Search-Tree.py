# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if val > node.val:
                if not node.right:
                    return
                node = node.right
            elif val < node.val:
                if not node.left:
                    return
                node = node.left
            else:
                return node

        