class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        contain = set()
        _min = float(inf)
        _max = float(-inf)

        for i in nums:
            _min = min(i, _min)
            contain.add(i)
            _max = max(i, _max)
        ans = []
        for i in range(_min, _max+1):
            if i not in contain:
                ans.append(i)
        return ans


        