class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # k zeros are allowed
        # consider a window with ones and zeros 
        # return max consecutive 1's
        window = {0:0, 1:0}
        j = 0
        ans = 0
        for i in range(len(nums)):
            window[nums[i]] += 1
            while window[0] > k:
                window[nums[j]] -= 1
                j += 1
            ans = max(ans, window[1]+k)
        return ans if ans <= len(nums) else len(nums)
                    