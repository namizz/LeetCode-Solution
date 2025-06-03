class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = min1 =product = nums[0]
        result = 0
        if not nums:
            return 0
        for i in range(1, len(nums)):
            temp = max(nums[i], max1* nums[i], min1 * nums[i])
            min1 = min(nums[i], max1* nums[i], min1 * nums[i])
            max1 = temp
            product = max(max1, product)
            
        return product