class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        cache = {}
        def rec(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            a = nums[i] + rec(i+2)
            b = nums[i] + rec(i+3)
            cache[i] = max(a,b)
            return cache[i]
        return max(rec(0), rec(1))
        