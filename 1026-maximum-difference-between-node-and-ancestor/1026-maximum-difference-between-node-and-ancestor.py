# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def diff_from_max(root):
            nonlocal ans
            if not root:
                return float(inf),float(-inf)
            if not root.left and not root.right:#if it is leave node
                return root.val, root.val
            min_left,max_left = diff_from_max(root.left)
            min_right,max_right = diff_from_max(root.right)
            _min, _max = min(min_left,min_right), max(max_left, max_right)
            ans = max([abs(root.val-_min), abs(root.val-_max),ans])
            # print(_min, _max, "ops = ", ans)
            return min(_min,root.val), max(_max,root.val)
        diff_from_max(root)
        return ans
        