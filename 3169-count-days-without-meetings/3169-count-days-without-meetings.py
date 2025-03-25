class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        m = sorted(meetings, key=lambda x:x[0])
        ans = 0
        prev = m[0][0]
        for s,e in m:
            prev = max(prev,s)
            if e-prev+1>0:
                ans += e-prev+1
            prev = max(prev, e+1)
            
        return days-ans





        