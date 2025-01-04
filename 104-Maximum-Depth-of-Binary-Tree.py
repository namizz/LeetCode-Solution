# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node):
            global depth
            if not node:
                return  0
            return 1+max(dfs(node.left), dfs(node.right))
        return dfs(root)

        