class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        hashmap = {}
        for i in range(len(sorted_nums)):
            if i <= 0 or sorted_nums[i-1] != sorted_nums[i]:
                hashmap[sorted_nums[i]] = i
        ans = []
        for num in nums:
            ans.append(hashmap[num]) 
        return ans
                