class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def rec(l,r):
            if l+1 >= r:
                return nums[l]          
            mid = (l+r)//2
            left = rec(l,mid)
            right = rec(mid,r)
            left_sum = float('-inf')
            temp = 0
            for i in range(mid - 1, l - 1, -1):
                temp += nums[i]
                left_sum = max(left_sum, temp)

            right_sum = float('-inf')
            temp = 0
            for i in range(mid, r):
                temp += nums[i]
                right_sum = max(right_sum, temp)

            cross = left_sum + right_sum

            return max(left, right, cross)
        return rec(0, len(nums))
        