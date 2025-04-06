class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #54331
        #13345
        i = 0
        ans = []
        while i < len(nums):
            idx = nums[i]-1 
            if idx+1 != nums[idx] and nums[idx] != nums[i]:
                nums[i], nums[idx] = nums[idx], nums[i]
            elif nums[i] == i+1:
                i += 1
            else:
                i += 1
        for i in range(len(nums)):
            if i+1 != nums[i]:
                ans.append(nums[i])
                ans.append(i+1)

        return list(ans)
            
        