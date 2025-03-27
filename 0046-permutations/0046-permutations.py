class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(path,arr):
            if not arr:
                ans.append(path[:])
                return 
            for i in range(len(arr)):
                backtrack(path+[arr[i]], arr[:i]+arr[i+1:])
        backtrack([],nums)
        return ans
        