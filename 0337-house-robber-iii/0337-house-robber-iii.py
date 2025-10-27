# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def rec(node):
            if not node:
                return 0
            if node in cache:
                return cache[node]

            ans = 0
            if node.left:
                ans += rec(node.left.left) + rec(node.left.right)
            if node.right:
                ans += rec(node.right.left) + rec(node.right.right)
            cache[node] = max(ans+ node.val, rec(node.left) + rec(node.right))
            return cache[node]
        return rec(root)



                


        
        