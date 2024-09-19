class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter = 0
        stack = []
        for i in range(len(s)): 
            if s[i] == "(":
                if counter > 0:
                    stack.append(s[i])
                    counter += 1
                elif counter == 0:
                    counter += 1
            else:
                if counter > 1:
                    stack.append(")")
                    counter -= 1
                else:
                    counter -= 1
        return "".join(stack)


        