class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # nums =[], queries = [[li, ri],...]
        # return true or false
        # iterate through queries
        # []*n+1
        # q[li] -= 1, q[ri+1] += 1
        # iterate through nums
        # prefix sum q:
        # prefix sum num
        # ps = num[i] + q[i]
        # if ps > 0 return false else iterate
        # return true
        q = [0]*(len(nums)+1)
        for li, ri in queries:
            q[li] -= 1
            q[ri+1] += 1
        if q[0]+nums[0] > 0:
            return False
        for i in range(1,len(nums)):
            q[i] += q[i-1]
            ps = nums[i]+q[i]
            if ps > 0:
                return False
        return True