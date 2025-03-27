class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        ans = float(inf)
        while l <= r:
            mid = (l+r)//2
            if nums[r] >= nums[mid]:
                ans = min(ans,nums[mid])
                r = mid -1
            else:
                l = mid + 1
        return ans