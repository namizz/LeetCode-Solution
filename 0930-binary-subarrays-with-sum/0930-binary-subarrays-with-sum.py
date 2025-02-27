class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = 0
        hashmap = {0:1}
        ans = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - goal in hashmap:
                ans += hashmap[prefix-goal]
            hashmap[prefix] = hashmap.get(prefix, 0) + 1
        return ans






        