class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)
        for i in range(len(nums)):
            if hashmap[nums[i]] > 1:
                return True
        return False

        