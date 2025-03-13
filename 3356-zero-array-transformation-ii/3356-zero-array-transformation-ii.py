class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # queries [l,r,v]--> decrease by value v from nums[l] to nums[r]
        # 
        _max = max(nums)
        j = 0
        while _max > 0:
            prefix = [0]*(len(nums)+1)
            temp = 0
            while temp < _max and j < len(queries):
                l,r,v = queries[j]
                temp += v
                prefix[l] -= v
                prefix[r+1] += v
                j += 1
            for i in range(1,len(prefix)):
                prefix[i] += prefix[i-1]
            _max = float(-inf)
            for i in range(len(nums)):
                nums[i] += prefix[i]
                _max = max(nums[i],_max)
            if j == len(queries) and _max > 0:
                return -1
        return j
        