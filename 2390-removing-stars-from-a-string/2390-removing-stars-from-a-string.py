class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for l in s:
            if l != "*":
                stack.append(l)
            elif stack:
                stack.pop()
        return "".join(stack)