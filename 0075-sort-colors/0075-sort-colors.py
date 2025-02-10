class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        for i in range(len(nums)):
            if nums[i] == 0 and p1 != i:
                nums[i], nums[p1] = nums[p1], nums[i]
            while p1 < i and nums[p1] == 0:
                p1 += 1
            
        print(nums, p1)
        for i in range(p1,len(nums)):
            if nums[i] == 1 and p1 != i:
                nums[i], nums[p1] = nums[p1], nums[i]
            while p1 < i and nums[p1] == 1:
                p1 += 1
        return nums


            
        