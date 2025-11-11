class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(i, xor):
            if i == len(nums):
                return xor
            
            take = backtrack(i+1, nums[i]^xor)
            no_take = backtrack(i+1,xor)
            return no_take+take
        return backtrack(0,0)



        