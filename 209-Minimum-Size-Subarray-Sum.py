class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # we need a var that store the sum(prefix sum) of window(sliding window)
        # window:-> window-size increase if the window sum is less
        # window:-> window-size decrease if the window sum is greater after the subtraction of left arr:-> nested loop
        # return the min answer with window size
        # ans is update after the nested loop
        start = 0
        end = 0
        total = 0
        ans = 0
        while end < len(nums):
            total += nums[end]
            end += 1
            if target <= total:
                while target <= total-nums[start]:
                    total -= nums[start]
                    start += 1
                if ans == 0:
                    ans = end - start
                ans = min(ans, end-start)
        return ans

        