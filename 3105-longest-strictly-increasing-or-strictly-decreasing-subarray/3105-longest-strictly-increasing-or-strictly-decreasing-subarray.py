class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 0
        temp = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                temp += 1
            else:
                temp = 1
            ans = max(temp, ans)
        temp = 1
        for i in range(len(nums)-1,0,-1):
            if nums[i] < nums[i-1]:
                temp += 1
            else:
                temp = 1
            ans = max(temp, ans)
        return max(temp, ans)
            
        