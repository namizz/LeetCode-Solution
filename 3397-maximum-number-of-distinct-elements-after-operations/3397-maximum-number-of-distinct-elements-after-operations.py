class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        ans = 0
        temp = float(-inf)
        for i in range(len(nums)):
            poss = max(nums[i]-k ,temp+1)
            if poss <= nums[i]+k:
                ans += 1
                temp = poss

        return ans

                