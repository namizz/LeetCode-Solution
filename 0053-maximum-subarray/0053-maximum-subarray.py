class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force is 
        # check for nums[0] -> len(nums[i])
        # -2, -1, -4, 0, -1, 1, 2, -3, 1
        # 0: -2, 1: -1, 2: -1, 3: 0, 4: 0, 5: 1, 6: 2, 7:2, 8:2
        c_sum = 0
        _max = float(-inf)
        for i in range(len(nums)):
            if c_sum < 0:
                c_sum = 0
            c_sum += nums[i]
            _max = max(c_sum, _max)
        return _max