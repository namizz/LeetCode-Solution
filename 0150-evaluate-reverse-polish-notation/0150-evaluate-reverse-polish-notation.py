class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def ops(op, x, y):
            if op == "+":
                return x + y
            elif op == "-":
                return y-x
            elif op == "*":
                return y*x
            else:
                return int(y/x)

        for i in tokens:
            if i in "+-*/":
                x = stack.pop()
                y = stack.pop()
                stack.append(ops(i,x,y))
            else:
                stack.append(int(i))
        return stack[0]
                
        