# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hashmap = {}
        def mode(tree):
            if not tree:
                return
            mode(tree.left)
            if tree.val in hashmap:
                hashmap[tree.val] += 1
            else:
                hashmap[tree.val] = 1
            mode(tree.right)
        mode(root)
        ans, m = [root.val], 0 
        for key in hashmap:
            if hashmap[key] > hashmap[ans[0]]:
                ans = [key]
            elif hashmap[key] == hashmap[ans[0]] and key != root.val:
                ans.append(key)

        return ans


        