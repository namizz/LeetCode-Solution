class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            if i == '(':
                stack.append('(')
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    while len(stack) > 1:
                        if stack[-2] != '(':
                            x = stack.pop()
                            y = stack.pop()
                            stack.append(x+y)
                        else: 
                            x = stack.pop()
                            stack.pop()
                            stack.append(2*x)
                            break
                    
                    
        return sum(stack)
