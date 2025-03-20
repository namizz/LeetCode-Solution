# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def average(root):
            nonlocal ans
            if not root:
                return 0,0
            left, nl = average(root.left)
            right, nr = average(root.right)

            _sum = root.val + left + right
            nodes = nr + nl +1
            if root.val == _sum//nodes:
                ans += 1
            return _sum, nodes
        average(root)
        return ans



            

        