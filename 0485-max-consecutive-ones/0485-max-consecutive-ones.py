class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        ans = 0
        for r in range(len(nums)):
            if not nums[r]:
                r += 1
                l = r
                continue
            ans = max(ans, r-l+1)
        return ans

        