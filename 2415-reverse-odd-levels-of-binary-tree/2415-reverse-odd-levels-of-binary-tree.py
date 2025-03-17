# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        j = 0
        while queue:
            temp = deque()
            if j%2 == 0:
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
            else:
                contain = []
                for l in queue:
                    contain.append(l.val)
                for i in range(len(queue)):
                    queue[0].val = contain[-i-1]
                    node = queue.popleft()
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
            queue = temp           

            j += 1
        return root
        