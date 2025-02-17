class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        running_sum = sum(nums)
        ans = 0
        for i in range(len(nums)):
            if i > 0 and running_sum - nums[i-1]-nums[i] == nums[i-1]:
                return i
            elif i == 0 and running_sum-nums[i] == 0:
                return 0
            elif i != 0:
                nums[i] += nums[i-1]
        return -1
        