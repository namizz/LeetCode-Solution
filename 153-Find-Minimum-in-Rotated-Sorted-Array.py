class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp ,rp= 0, len(nums)-1
        mid = -1
        while lp < rp:
            mid = (lp + rp)//2
            if nums[lp] <= nums[mid] and nums[mid] <= nums[rp]:
                return nums[lp]
            elif nums[rp] <= nums[lp] and nums[lp] <= nums[mid]:
                lp = mid + 1
            else:
                rp = mid
        return min(nums[mid], nums[lp], nums[rp])
        