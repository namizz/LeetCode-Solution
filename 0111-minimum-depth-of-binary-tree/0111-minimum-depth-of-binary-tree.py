# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            temp = deque()
            depth += 1
            while queue:
                node= queue.popleft()
                if not node.right and not node.left:
                    return depth
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
        return depth


        