class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        container = set()
        for i in nums:
            if i in container:
                return True
            else:
                container.add(i)
        return False

        