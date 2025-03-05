class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {"(":")", "[":"]", "{":"}"}
        for b in s:
            if b == "(" or b =="[" or b == "{":
                stack.append(b)
            elif stack:
                if hashmap[stack[-1]] == b:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return not stack
        