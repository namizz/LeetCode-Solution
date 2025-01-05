class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #circular array
        # nums: []
        # return next greater elememt
        # iterate until it get next greater element
        stack = []
        ans = [0]*len(nums)
        for i in range(2*len(nums)-1,-1,-1):
            while stack and stack[-1] <= nums[i%len(nums)]:
                stack.pop()
            if not stack:
                ans[i%len(nums)] = -1
            else:
                ans[i%len(nums)] = stack[-1]
            stack.append(nums[i%len(nums)])       

        return ans



