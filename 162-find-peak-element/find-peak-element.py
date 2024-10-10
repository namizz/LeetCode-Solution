class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:  return 0
        if nums[0] > nums[1]:  return 0
        if nums[-1] > nums[-2]:  return len(nums)-1
        
        lp, rp = 0, len(nums) - 1
        while lp+1 < rp:
            mid = (lp + rp)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid-1] < nums[mid]:
                lp = mid + 1
            else:
                rp = mid - 1
        return lp if nums[lp] > nums[rp] else rp
        