class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        size=len(nums)
        for i in range(0,size-1):
            if nums[i]==nums[i+1]:
                nums[i]=2*nums[i]
                nums[i+1]=0
        count=0
        for index in range(size):
            if nums[index]:
                nums[count],nums[index]=nums[index],nums[count]
                count+=1
        return nums
        