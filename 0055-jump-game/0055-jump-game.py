class Solution:
    def canJump(self, nums: List[int]) -> bool:
        checker = 0
        last_zero = False
        if nums == [0]:
            return True
        for i in range(len(nums)-1, -1,-1):
            if nums[i] == 0:
                if i == len(nums)-1:
                    last_zero = True
                checker += 1
            elif last_zero and checker <= nums[i]:
                checker = 0 
                last_zero = False
            elif checker and checker < nums[i]:
                checker = 0
            elif checker:
                checker += 1
        
        return not checker




        