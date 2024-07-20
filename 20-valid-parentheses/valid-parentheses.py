class Solution:
    def isValid(self, s: str) -> bool:
        order = 0
        check = 0
        result = 0
        x = 0
        y = 0
        z =0
        for i in s:
            if i == '[' or i == '{' or i == '(':
                order += 1
                check += 1
                if i == '(':
                    x += order
                elif i == '{':
                    y += order
                else:
                    z += order
            elif i == ']' or i == '}' or i == ')':
                check -= 1
                if i == ')':
                    x -= order
                elif i == '}':
                    y -= order
                else:
                    z -= order
                order -= 1
                print(x,y,z)
            if (check < 0) or (x < 0) or (y < 0) or (z < 0):
                return False
                break

        if x == 0 and y ==0 and z == 0 :
            return True


