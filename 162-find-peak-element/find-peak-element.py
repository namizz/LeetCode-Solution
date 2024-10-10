class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums) - 1
        # lp = 0
        # rp = len(nums) - 1
        # while lp < rp-1:
        #     mid = (lp + rp)//2
        #     print(lp, mid, rp)
        #     if nums[lp] < nums[mid] and nums[mid] < nums[rp]:
        #         lp += 1
        #         if nums[lp-1] > nums[lp]:
        #             return lp-1
        #     else:
        #         if nums[lp] > nums[mid]:
        #             rp = mid
        #         else:
        #             lp = mid
        # return lp if len(nums) > 1 and nums[lp] > nums[lp+1] else len(nums) - 1
        