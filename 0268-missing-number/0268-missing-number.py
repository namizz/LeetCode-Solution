class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans ^= i
            ans ^= nums[i]
        return ans ^ len(nums)
        

        