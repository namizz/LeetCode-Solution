# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        prev = root
        deleted = root
        while deleted and deleted.val != key:
            prev = deleted
            if deleted.val > key:
                deleted = deleted.left
            else:
                deleted = deleted.right
        if deleted:
            if deleted.right:
                rep = deleted.right
                rep_prev = deleted
                while rep.left:
                    rep_prev = rep
                    rep = rep.left
                rep.val, deleted.val = deleted.val, rep.val
                if rep.right:
                    if rep_prev.left == rep:
                        rep_prev.left = rep.right
                    else:
                        rep_prev.right = rep.right
                elif rep_prev.right and rep_prev.right== rep:
                    rep_prev.right = None
                else:
                    rep_prev.left = None
            elif deleted.left:
                if deleted == prev:
                    root = deleted.left
                else:
                    prev.left = deleted.left
            elif prev.left and prev.left == deleted:
                prev.left = None
            elif not prev.right and not prev.left:
                return prev.left
            else:
                prev.right = None

        return root


        