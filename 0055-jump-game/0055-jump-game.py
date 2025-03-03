class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = [0]*(len(nums)+1)
        if nums == [0]:
            return True
        for i in range(len(nums)):
            ans[i] += 1
            if nums[i]+i < len(nums): 
                ans[nums[i]+i] -= 1
    
        for i in range(len(nums)-1):
            if i != 0:
                ans[i] += ans[i-1]
            if ans[i] == 0:
                return False
        return True

        




        