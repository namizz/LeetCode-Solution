class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = (n*(n+1))//2
        for i in range(n):
            s -= nums[i]
        return s
        

        