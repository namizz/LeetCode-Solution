class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        contain = set()
        ans = []
        for num in nums:
            if num in contain:
                ans.append(num)
            else:
                contain.add(num)
        return ans
        