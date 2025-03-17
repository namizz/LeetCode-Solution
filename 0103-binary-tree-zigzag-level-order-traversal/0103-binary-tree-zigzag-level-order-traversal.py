# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        zig = True
        queue = deque([root])
        ans = []
        while queue:
            temp = deque()
            a = []
            for v in queue:
                a.append(v.val)
            ans.append(a if zig else a[::-1])
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            zig = not zig
            queue = temp
        # 23
        return ans                


        