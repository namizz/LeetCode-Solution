# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #down add
        #if it isn't valid start to go up and get subtracted the ps
        if not root:
            return False
        queue = deque([(root.val, root)])
        while queue:
            for _ in range(len(queue)):
                ps, node = queue.popleft()
                if not node.left and not node.right:
                    if ps == targetSum:
                        return True
                if node.left:
                    queue.append((ps+node.left.val, node.left))
                if node.right:
                    queue.append((ps+node.right.val, node.right))
        return False
        