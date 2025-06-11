class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        i = 1
        counter = 1
        n = len(nums)
        while i < n:
            if nums[pointer] != nums[i]:
                nums[counter] = nums[i]
                pointer = i
                counter += 1
            i += 1
        return counter