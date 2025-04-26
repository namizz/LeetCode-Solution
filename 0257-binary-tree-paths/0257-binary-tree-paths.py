# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        temp = []
        def dfs(node):
            if not node:
                return
            temp.append(str(node.val))
            if not node.left and not node.right:
                ans.append("->".join(temp))
            else:
                dfs(node.left)
                dfs(node.right)
            temp.pop()
        dfs(root)
        return ans
        