class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        container = set(nums)
        for i in range(len(nums)):
            if i not in container:
                return i
        return len(nums)

        