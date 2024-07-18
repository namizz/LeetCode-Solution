class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cs = sum(nums[:k])
        max_sum = cs
        for end in range(k,len(nums)):
            cs += nums[end]
            cs -= nums[end-k]
            max_sum = max(cs,max_sum)
        return max_sum/k



        