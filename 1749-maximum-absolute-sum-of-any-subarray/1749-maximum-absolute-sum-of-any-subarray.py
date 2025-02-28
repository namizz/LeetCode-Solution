class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        _max, _min = 0, 0
        for i in range(len(nums)):
            if i != 0: 
                nums[i] += nums[i-1]
            _max = max(nums[i],_max)
            _min = min(nums[i],_min)
        return _max-_min 
        