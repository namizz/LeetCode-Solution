class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):

            while stack and stack[-1][0] < temperatures[i]:
                x = stack.pop()
                ans[x[1]] = i - x[1]
            stack.append((temperatures[i],i))
        return ans
        