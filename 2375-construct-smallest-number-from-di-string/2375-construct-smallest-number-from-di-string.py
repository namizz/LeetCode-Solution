class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        stack = []
        k = 1
        for i in range(len(pattern)):
            stack.append(k)
            k += 1
            if pattern[i] == "I":
                while stack:
                   ans.append(stack.pop())
        stack.append(k)
        while stack:
            ans.append(stack.pop())
            
        return "".join(map(str,ans))



        