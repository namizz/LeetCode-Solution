class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = 1 if nums[i]%2 else 0
        hashmap = {0:1}
        prefix = 0
        ans = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix-k in hashmap:
                ans += hashmap[prefix-k]
            hashmap[prefix] = hashmap.get(prefix, 0)+1
        return ans 


        