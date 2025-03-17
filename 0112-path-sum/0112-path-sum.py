# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(root, ans=0):
            if not root:
                return False
            ans += root.val
            if not (root.left or root.right) and targetSum == ans:
                return True
            return dfs(root.left, ans) or dfs(root.right, ans)
        return dfs(root) 
        