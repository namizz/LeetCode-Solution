class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = [0]*100
        def ss(x):
            return (x*(x+1))//2
        for i in range(len(nums)):
            if ans[nums[i]] < 0:
                ans[nums[i]] = 1
            elif ans[nums[i]] > 0:
                ans[nums[i]] += 1
            else:
                ans[nums[i]] = -1
        return sum(ss(i) if i > 0 else 0 for i in ans)


        