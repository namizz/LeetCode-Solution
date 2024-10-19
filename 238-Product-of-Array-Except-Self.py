class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = [1]* len(nums)
        l = 1
        for i in range(len(nums)):
            a[i] = l
            l *= nums[i]
        r = 1
        for i in range(len(nums)-1,-1,-1):
            a[i] *= r
            r*= nums[i]
        return a



        