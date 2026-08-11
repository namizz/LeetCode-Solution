class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        contain = set(nums)
        i = 1
        ans = nums[0]
        while i < len(nums) and nums[i-1] + 1 == nums[i]:
            ans += nums[i]
            i += 1
        while ans in contain:
            ans += 1
        

        return ans
        