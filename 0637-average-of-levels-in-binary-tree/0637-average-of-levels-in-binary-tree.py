# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        av = 0
        queue = deque([root])
        ans = []
        while queue:
            n = len(queue)
            for i in range(n):
                x = queue.popleft()
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
                av += x.val
            ans.append(av/n)
            av = 0

        return ans
        