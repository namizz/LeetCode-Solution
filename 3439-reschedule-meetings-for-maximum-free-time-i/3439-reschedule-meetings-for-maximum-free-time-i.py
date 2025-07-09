class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        ans = 0
        total = [0] * (len(startTime)+1)
        for i in range(len(startTime)):
            total[i+1] = total[i] + endTime[i] - startTime[i]
        print(total)
        for i in range(k-1, len(startTime)):
            r = eventTime if i == len(startTime)-1 else startTime[i+1]
            l = 0 if i == k-1 else endTime[i-k]
            print("rl", r,l)
            ans = max(ans, r-l-(total[i+1]-total[i-k+1]))
            print(ans)
        return ans
        