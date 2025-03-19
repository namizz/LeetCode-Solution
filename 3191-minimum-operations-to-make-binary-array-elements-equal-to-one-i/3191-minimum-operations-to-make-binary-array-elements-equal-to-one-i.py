class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # goal to make 1 array
        # flip 3 consecutive sub-array
        #  [0,1,0,1,1]
        #  ``````
        #  [1,2,3,2,1]
        # 
        prefix = [0]*(len(nums)+1)
        ans = 0
        for i in range(len(nums)):
            if i > 0:
                prefix[i] += prefix[i-1]
            if not (nums[i]+prefix[i])%2:
                ans += 1
                prefix[i] += 1
                if i+3 >= len(prefix):
                    return -1
                prefix[i+3] -= 1
        return ans

        