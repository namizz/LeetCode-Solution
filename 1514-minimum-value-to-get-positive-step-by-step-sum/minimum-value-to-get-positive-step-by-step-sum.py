class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start_value = 1
        ps = 1
        for i in range(len(nums)):
            ps += nums[i]
            if ps < 1:
                start_value = start_value + abs(ps) + 1
                ps = 1
        return start_value
                
        