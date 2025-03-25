class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find a target that it left != target
        if not nums:
            return [-1,-1]
        def left():
            lp, rp = 0,len(nums)-1
            while lp <= rp:
                mid = (lp+rp)//2
                if nums[mid] < target:
                    lp = mid + 1
                else:
                    rp = mid - 1
            # print(lp)
            return lp if lp < len(nums) and nums[lp] == target else -1
        def right():
            lp, rp = 0,len(nums)-1
            while lp <= rp:
                mid = (lp+rp)//2
                if nums[mid] > target:
                    rp = mid - 1
                else:
                    lp = mid + 1
            # print(rp)
            return rp if 0<= rp and nums[rp] == target else -1
        return [left(),right()]
        
        
            

        