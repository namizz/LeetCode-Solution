class Solution:
    def maximumCandies(self, candies, k):
        def check(x):
            pos = 0
            for i in candies:
                pos += (i//x)
            return pos >= k

        l, r = 1, max(candies)
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
