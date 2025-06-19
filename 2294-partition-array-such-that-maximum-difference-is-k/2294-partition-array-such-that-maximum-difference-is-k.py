class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        mi = nums[0]
        mx = nums[0]
        ans = 1
        for i in range(len(nums)):
            mi = min(mi,nums[i])
            mx = max(mx,nums[i])
            if mx-mi <= k:
                continue
            else:
                mi = nums[i]
                mx = nums[i]
                ans += 1

        return ans
        






        
        
        return

        