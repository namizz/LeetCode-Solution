class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[left] = nums[left], nums[i]
                left+=1
                
        print(nums)