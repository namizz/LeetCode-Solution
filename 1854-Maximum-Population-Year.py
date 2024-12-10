class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        c = [0]*2101
        mans = 0
        ans = 0
        for birth, death in logs:
            c[birth-1950] += 1
            c[death-1950] -= 1
        for i in range(len(c)):
            if i > 0:
                c[i] += c[i-1]
            if mans < c[i]:
                mans = c[i]
                ans = i
        return ans + 1950

        
        