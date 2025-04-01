# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        print(arr)
        def bst(arr):
            if not arr:
                return None

            mid = len(arr)//2
            rt = TreeNode(arr[mid])
            rt.left = bst(arr[:mid])
            rt.right = bst(arr[mid+1:])
            return rt
        return bst(arr) if arr else TreeNode(0)
        