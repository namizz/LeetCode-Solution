class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sliding window won't be effective if there is negative number in array
        # hashmap --> store prefix sum and there frequency
        # prefix sum - k in hashmap
        hashmap = {0:1}
        total = 0
        ans = 0
        for i in range(len(nums)):
            total += nums[i]
            if total - k in hashmap:
                ans += hashmap[total-k]
            
            if total in hashmap:
                hashmap[total] += 1
            else:
                hashmap[total] = 1
        return ans
