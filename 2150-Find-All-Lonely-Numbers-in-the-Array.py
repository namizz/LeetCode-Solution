class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        contain = set()
        hashmap = Counter(nums)
        for i in range(len(nums)):
            if hashmap[nums[i]] > 1:
                contain.add(nums[i])
            if nums[i] - 1 in hashmap:
                contain.add(nums[i] - 1)
            if nums[i] + 1 in hashmap:
                contain.add(nums[i] + 1)
        ans = []
        for i in range(len(nums)):
            if nums[i] not in contain:
                ans.append(nums[i])
        return ans
        