class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        ans = 0
        for i in range(len(nums)):
            if not nums[i]:
                if left == right:
                    ans += 2
                elif abs(left-right) == 1:
                    ans += 1
            else:
                left += nums[i]
                right -= nums[i]
                
        return ans



        