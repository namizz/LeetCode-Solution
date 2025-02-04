class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        for i in range(len(nums)):
            if hashmap[nums[i]] > len(nums)//2:
                return nums[i]
        