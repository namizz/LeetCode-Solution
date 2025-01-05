class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #circular array
        # nums: []
        # return next greater elememt
        # iterate until it get next greater element
        ans = []
        numss = nums*2
        for i in range(len(nums)):
            j = i+1
            while j < len(numss):
                if nums[i] < numss[j]:
                    ans.append(numss[j])
                    break
                j += 1
            if len(ans)-1 < i:
                ans.append(-1)
        return ans 
