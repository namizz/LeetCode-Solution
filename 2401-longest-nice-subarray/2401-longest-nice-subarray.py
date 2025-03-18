class Solution:
    def longestNiceSubarray(self, nums):
        l = 0
        usedBits = 0
        maxLength = 0

        for r in range(len(nums)):
            while (usedBits & nums[r]) != 0:
                usedBits ^= nums[l]
                l += 1

            usedBits |= nums[r]
            maxLength = max(maxLength, r - l + 1)

        return maxLength