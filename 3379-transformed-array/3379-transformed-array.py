class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):
            pos = nums[i] if nums[i] != 0 else 0 
            result[i] = nums[(i+pos)% len(nums)] 
        return result