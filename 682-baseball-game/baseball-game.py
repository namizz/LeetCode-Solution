class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == '+':
                x = stack.pop()
                y = stack.pop()
                stack.append(y)
                stack.append(x)
                stack.append(x+y)
            elif operations[i] == 'C':
                stack.pop()
            elif operations[i] =='D':
                x = stack.pop()
                stack.append(x)
                stack.append(x*2)
            else:
                stack.append(int(operations[i]))
        ans = 0
        while stack:
            ans += stack.pop()
        return ans

            
                

        