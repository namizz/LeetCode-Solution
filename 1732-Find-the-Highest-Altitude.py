class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        ps = 0
        for i in gain:
            ps += i
            ans = max(ans, ps)
        return ans

        