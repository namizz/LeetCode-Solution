class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        st = [s for s,_,_ in events]
        dp = [[0]* (len(events)+1) for _ in range(k+1)]
        for curr in range(len(events) - 1, -1, -1):
            for count in range(1, k + 1):
                nxt = bisect_right(st, events[curr][1])
                dp[count][curr] = max(dp[count][curr + 1], events[curr][2] + dp[count - 1][nxt])
        return dp[k][0]
        