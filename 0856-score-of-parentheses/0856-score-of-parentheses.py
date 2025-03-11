class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        total = 0
        for i in range(len(s)):
            if s[i] =='(':
                stack.append(total)
                total = 0
            else:
                if total == 0:
                    total =  stack.pop() + 1
                else:
                    total = total*2 + stack.pop()
                    

        return total

        