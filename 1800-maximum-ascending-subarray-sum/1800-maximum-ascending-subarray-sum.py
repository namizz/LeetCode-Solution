class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        temp = nums[0]
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                temp += nums[i+1]
            else:
                ans = max(temp, ans)
                temp = nums[i+1]
        return max(ans, temp)

            
                    
        