class Solution:
    def maxDepth(self, s: str) -> int:
        # we increase count when we get '(' decrease when we get ')':
        stack = []
        count = 0
        for i in range(len(s)):
            if '(' == s[i]:
                stack.append(s[i])
                count = max(len(stack), count)
            elif ')' == s[i]:
                if stack:
                    stack.pop()
        return count

        