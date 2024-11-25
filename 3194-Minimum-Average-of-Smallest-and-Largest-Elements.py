class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        lp = 0
        rp = len(nums)-1
        ans = 0
        while lp < rp:
            if ans == 0:
                ans = (nums[lp] + nums[rp])/2
            ans = min((nums[lp]+nums[rp])/2, ans)
            lp += 1
            rp -= 1
        return ans

        
        