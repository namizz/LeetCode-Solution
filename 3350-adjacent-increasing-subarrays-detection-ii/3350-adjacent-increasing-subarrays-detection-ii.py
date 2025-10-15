class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        c1 = 1
        c2 = 1
        dec = 0
        ans = 0
        for i in range(1, len(nums)):
            if not dec and nums[i-1] < nums[i]:
                c1 += 1
            elif dec and nums[i-1] < nums[i]:
                c2 += 1
            elif not dec:
                dec = 1
            else:
                ans = max(ans, c1//2, c2//2, min(c1,c2))
                c1 = c2
                c2 = 1
                dec = 1
        return  max(ans, c1//2, c2//2, min(c1,c2))
            


        