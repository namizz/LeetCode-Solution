class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        ans = []
        for k,v in hashmap.items():
            if v == 2:
                ans.append(k)
        return ans
        