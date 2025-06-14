class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        l= 0
        r = len(queries)
        def valid(mid):
            temp = [0]*len(nums) +[0]
            for i in range(mid):
                l,r,val = queries[i]
                temp[l] += val
                temp[r+1] -= val
            for i in range(len(nums)):
                if i > 0:
                    temp[i] += temp[i-1]
                if temp[i] < nums[i]:
                    return False
            return True
        ans = -1
        while l <= r:
            mid = (l + r)//2
            if valid(mid):
                ans = mid
                r = mid - 1 
            else:
                l = mid + 1
        return ans
            



        