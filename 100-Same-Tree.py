# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (not q and p):
            return False
        elif not p and not q:
            return True
        queue1 = deque([p])
        queue2 = deque([q])
        while queue1 and queue2:
            for i in range(max(len(queue1), len(queue2))):
                if len(queue1) != len(queue2):
                    return False
                n1 = queue1.popleft()
                n2 = queue2.popleft()
                if n1.val != n2.val:
                    return False
                if n1.left or n2.left:
                    if not n2.left or not n1.left or n2.left.val != n1.left.val:
                        return False
                    queue1.append(n1.left)
                    queue2.append(n2.left)
               
                if n2.right or n1.right:
                    if not n2.right or not n1.right or n2.right.val != n1.right.val:
                        return False 

                    queue2.append(n2.right)
                    queue1.append(n1.right)
                
            print(queue1, queue2)
        return True 



        