class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        ans = []
        hashmap = Counter(nums)
        for i in range(len(nums)):
            if hashmap[nums[i]] > 1 or nums[i] - 1 in hashmap or nums[i] + 1 in hashmap:
                continue
            ans.append(nums[i])
        return ans
        