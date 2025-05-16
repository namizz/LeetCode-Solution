class Solution:
    def longestNiceSubarray(self, nums):
        ans = 0
        lp = 0
        bt = 0
        for rp in range(len(nums)):
            while bt & nums[rp]:
                bt ^= nums[lp]
                lp += 1
            bt |= nums[rp]
            ans = max(ans, rp - lp + 1)
        return ans
        