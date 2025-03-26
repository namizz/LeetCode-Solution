class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(path):
            if len(path) == 2*n:
                ans.append("".join(path))
                return
            if path.count('(') < n:
                backtrack(path+['('])
            if path.count(')') < path.count('('):
                backtrack(path+[')'])
        backtrack([])
        return ans
        