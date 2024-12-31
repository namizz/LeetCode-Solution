# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mode = []
        value = 0
        count = 0
        max_c = 0
        def inorder(tree):
            nonlocal max_c, value, mode, count
            if not tree:
                return
            inorder(tree.left)
            if tree.val == value:
                count += 1
            else:
                value = tree.val
                count = 1
            if count > max_c:
                mode = [value]
                max_c = count
            elif count == max_c:
                mode.append(value)
            inorder(tree.right)
            
        inorder(root)
        return mode

        