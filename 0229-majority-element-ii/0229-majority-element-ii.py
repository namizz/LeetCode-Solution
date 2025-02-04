class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        ans = []
        for k,v in hashmap.items():
            if v > len(nums)//3:
                ans.append(k)
        return ans
        