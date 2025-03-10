class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # nums
        # return the minimum maximum number
        # [2,7,9,6]
        # 
        ans = 0
        i = 0
        temp = 0
        while i < len(nums)-1:
            temp += nums[i]
            i += 1
            ans = max(ceil(temp/i), ans)
        return ans
