class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        appear = len(nums) // 3
        ans = []

        for i in hashmap:
            if hashmap[i] > appear:
                ans.append(i)
        return ans
