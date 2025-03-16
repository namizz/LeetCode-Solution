# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        ans = []
        while queue:
            _max = float(-inf)
            temp = deque()
            while queue:
                node = queue.popleft()
                _max = max(node.val, _max)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            ans.append(_max)
            queue = temp

        return ans
        
        