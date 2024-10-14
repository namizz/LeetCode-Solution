class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        knum = sum(nums[:k])
        total = knum
        for i in range(len(nums)-k):
            knum = knum - nums[i] + nums[i+k]
            total = max(knum, total)
        return total/k



        