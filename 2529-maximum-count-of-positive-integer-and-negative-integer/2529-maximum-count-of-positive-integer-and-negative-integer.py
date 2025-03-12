class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # find the last negative int
        #[-2,-1,-1,0,0,0,1]
        #     |
        def negative(l,r):
            while l <= r:
                mid= (l+r)//2
                if nums[mid] >= 0:
                    r = mid-1
                else:
                    l = mid+1
            return r
        def postive(l,r):
            while l <= r:
                mid= (l+r)//2
                if nums[mid] <= 0:
                    l = mid+1
                else:
                    r = mid-1
            return l
        n = len(nums)
        return max(negative(0,n-1) + 1, n-postive(0, n-1))

        # find the first postive int
        