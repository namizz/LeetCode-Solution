class Solution:
    def calculate(self, s: str) -> int:
        # change to postfix in stack and calculate by poping
        #322*+
        #352/
        def postfix_fun(s: str):
            stack = [] 
            output = []
            precedence = {'+': 1, '-': 1, '*': 2, '/': 2}  
            i = 0
            while i < len(s):
                if s[i] == ' ':
                    i += 1
                    continue
                if s[i].isdigit():
                    num = []
                    while i < len(s) and s[i].isdigit():
                        num.append(s[i])
                        i += 1
                    output.append("".join(num))  
                    continue  

                if s[i] in precedence:
                    while (stack and stack[-1] in precedence and 
                           precedence[stack[-1]] >= precedence[s[i]]):
                        output.append(stack.pop())
                    stack.append(s[i])
                
                i += 1          
            while stack:
                output.append(stack.pop())
            
            return output

        postfix = postfix_fun(s)
        num = []
        for i in postfix:
            if i.isdigit():
                num.append(i)
            else:
                y = int(num.pop())
                x = int(num.pop())
                if i== "/":
                    num.append(x//y)
                elif i == "*":
                    num.append(x*y)
                elif i == "+":
                    num.append(x+y)
                else:
                    num.append(x-y)
        return int(num[0])
                
                



                    


        