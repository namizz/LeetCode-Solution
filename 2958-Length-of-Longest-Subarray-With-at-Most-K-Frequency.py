class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        hashmap = {}
        ans = 0
        for right in range(len(nums)):
            hashmap[nums[right]] = hashmap.get(nums[right],0) + 1 
            while hashmap[nums[right]] > k:
                hashmap[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return max(ans, len(nums)- left)
        