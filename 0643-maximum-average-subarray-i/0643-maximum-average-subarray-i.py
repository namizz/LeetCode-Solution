class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        ans = float(-inf)
        total += sum(nums[:k-1])
        for i in range(k-1,len(nums)):
            total += nums[i]
            ans = max(total, ans)
            total -= nums[i-k+1]
        return ans/k
            
        

        