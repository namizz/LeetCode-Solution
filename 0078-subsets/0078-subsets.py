class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, path = [], []
        def sub(i, combination):
            if i >= len(nums):
                ans.append(combination[:])
                return
            combination.append(nums[i])
            sub(i+1, combination)
            combination.pop()
            sub(i+1, combination)
        sub(0,[])
        return ans
        