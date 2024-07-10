class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = 0
        n = 0

        while n < len(nums):
            if nums[n]:
                nums[n], nums[zeros] = nums[zeros], nums[n]
                zeros+=1
            n +=1
                
        print(nums)