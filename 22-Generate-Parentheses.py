class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def rec(path):
            if len(path) >= n*2:
                ans.append("".join(path))
                return
            if path.count('(') < n:
                rec(path+['('])
            if path.count(')') < path.count('('):
                rec(path+[')'])
        rec([])
            
        return ans

        