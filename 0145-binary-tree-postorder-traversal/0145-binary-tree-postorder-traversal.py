# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        def postorder(root):
            if not root.left and not root.right:
                return root.val
            if root.left:
                ans.append(postorder(root.left))
            if root.right:
                ans.append(postorder(root.right))
            return root.val
        postorder(root)
        return ans + [root.val]

        