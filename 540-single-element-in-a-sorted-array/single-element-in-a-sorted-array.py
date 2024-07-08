class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums) - 1 
        while rp != 0:
            if (rp-lp) == 2:
                if nums[lp] == nums[lp + 1]:
                    return nums[rp]
                return nums[lp]

            mid = (lp + rp)//2
            if nums[mid] == nums[mid - 1]:
                if mid%2 == 0:
                    rp = mid 
                else:
                    lp = mid + 1  
            elif nums[mid] == nums[mid + 1]:
                if mid%2 == 0:
                    lp = mid 
                else:
                    rp = mid - 1   
            else:
                return nums[mid]
        return nums[rp]