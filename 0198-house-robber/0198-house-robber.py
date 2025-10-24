class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        if not len(nums)-1:
            return dp[-1]
        dp[1] = max(nums[1], nums[0])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
        