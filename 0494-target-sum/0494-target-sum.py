class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def rec(i,tot):
            if i >= len(nums):
                if tot == target:
                    return 1
                return 0
            if (i, tot) in cache:
                return cache[(i,tot)]
            a = rec(i+1, tot+nums[i])
            s = rec(i+1, tot-nums[i])
            cache[(i,tot)] = a+s
            return cache[(i, tot)]
        return rec(0,0)
        