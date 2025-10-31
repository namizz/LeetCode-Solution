class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        res = []
        for k,v in hashmap.items():
            if v == 2:
                res.append(k)
        return res
        