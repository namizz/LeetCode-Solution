class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i < len(nums):
            pos = nums[i] - 1
            if i+1 != nums[i] and nums[pos] != nums[i]:
                nums[pos], nums[i] = nums[i], nums[pos]
            elif nums[pos] == nums[i] and i != pos:
                ans.append(nums[i])
                i += 1
            else:
                i += 1
        return list(set(ans))
            



        
