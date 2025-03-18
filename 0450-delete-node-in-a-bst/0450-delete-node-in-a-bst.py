# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def search(root):
            if not root:
                return None
            if root.val == key:
                if not root.left and not root.right:
                    return None
                elif root.right and not root.left:
                    return root.right
                elif root.left and not root.right:
                    return root.left
                else:
                    replaced = root.right
                    added = root.left
                    temp = replaced
                    while temp.left:
                        temp = temp.left
                    root.val = temp.val
                    temp.val = key
                    root.right = search(root.right)
                    return root
            elif root.val > key:
                root.left = search(root.left)
                return root
            else:
                root.right = search(root.right)
                return root

        root = search(root)
        return root


        