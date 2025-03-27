class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if nums[r] >= nums[mid]:
                ans = nums[mid]
                r = mid -1
            else:
                l = mid + 1
        return ans