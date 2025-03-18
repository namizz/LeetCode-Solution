# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
        ans= 0
        def adder(temp):
            num = int("".join(list(map(str, temp))))
            return num
       
        def summer(root):
            nonlocal ans
            if not root:
                return 
            stack.append(root.val)
            if not root.left and not root.right:
                ans += adder(stack)
            left = summer(root.left)
            right = summer(root.right)
            stack.pop()
        summer(root)
        return ans
            

        