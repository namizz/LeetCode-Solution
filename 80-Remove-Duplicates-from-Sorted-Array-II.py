class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        for num in nums:
            # Check if we can write this number:
            # Either it's the first two elements, or it's not the same as the element two positions before
            if p < 2 or num != nums[p - 2]:
                nums[p] = num
                p += 1
        
        return p