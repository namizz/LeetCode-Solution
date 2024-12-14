class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # tokens = [] in reverse polish notation
        # evalute the result 
        # + , - , / , *
        # we only need two inputs to evalute
        # 2, 1 , + = 3
        # 3 , 2, * = 6, 2 + = 8 
        # we are gonna use stack dsa 
        # if the string is a number we store w
        # if the string is operation we pop two elements from stack and evalute it 
        # store evaluted value in stack
        stack = []
        operation = {\+\,\-\,\/\,\*\}
        def evaluate(x,y,o):
            if o == \+\:
                return x+y
            elif o == \-\:
                return x-y
            elif o ==\*\:
                return x*y
            else:
                return int(x/y)
        for s in tokens:
            if s in operation:
                y = stack.pop()
                x = stack.pop()
                stack.append(evaluate(x,y,s))
            else:
                stack.append(int(s))
        return stack[0]
