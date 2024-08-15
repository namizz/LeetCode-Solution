class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i]== '{':
                stack.append(s[i])
            else:
                if stack and ((s[i] == ')' and stack.pop() == '(') or (s[i]== ']' and stack.pop()=='[') or (s[i]== '}'and stack.pop() == '{')):
                    continue
                else:
                    return False
        if stack:
            return False
        return True
                
        

