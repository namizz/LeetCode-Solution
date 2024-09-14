class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        ans = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(len(ans))
            elif s[i] == ')':
                y = len(ans)
                x = stack.pop()
                ans[x:y] = ans[x:y][::-1]

            
            else:
                ans.append(s[i])
            i += 1
        return "".join(ans)
        