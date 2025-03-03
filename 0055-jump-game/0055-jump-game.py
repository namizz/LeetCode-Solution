class Solution:
    def canJump(self, nums: List[int]) -> bool:
        temp = 0
        for i in range(len(nums)):
            if temp >= len(nums)-1:
                return True
            if nums[i] == 0 and temp <= i:
                return False
            temp = max(nums[i]+i,temp)
        return False


        




        