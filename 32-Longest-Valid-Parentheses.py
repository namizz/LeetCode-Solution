class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def valid_range(s) -> list:
            stack = []
            valid = []
            for i in range(len(s)):
                if s[i] == "(":
                    stack.append(i)
                elif stack and s[i] == ")":
                    nx,ny = [stack.pop(), i]
                    if valid:
                        x,y = valid[-1]
                        # embrass
                        if nx < x:
                            valid[-1] = [nx,ny]
                            if len(valid) > 1:
                                yy = valid[-2][1]
                                if yy+1 == nx:
                                    valid[-2][1] = ny
                                    valid.pop()
                                

                        # consequtive
                        elif nx-1 == y:
                            valid[-1] = [x,ny]
                        else:
                            valid.append([nx,ny])
                    else:
                        valid.append([nx,ny])
            return valid
        def ans(valid):
            _max = 0
            for x,y in valid:
                _max = max(y-x+1, _max)
            return _max
        return ans(valid_range(s))


        