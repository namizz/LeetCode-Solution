class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                ans.append(nums[i] * 2)
                ans.append(0)
                i += 1
            else:
                ans.append(nums[i])
            i += 1
        zeros = 0
        for i in range(len(ans)):
            if ans[i] == 0 and ans[zeros] != 0:
                zeros = i
            elif ans[zeros] == 0 and ans[i] != 0:
                ans[i], ans[zeros] = ans[zeros], ans[i]
                zeros += 1
        return ans
