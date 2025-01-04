# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #down add
        #if it isn't valid start to go up and subtract the node below
        if not root:
            return False
        def dfs(node, rs):
            if not node:
                return False
            rs += node.val
            if not node.right and not node.left:
                return rs == targetSum
            return dfs(node.left,rs) or dfs(node.right,rs)
        return dfs(root, 0)
        