class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] 
        k = float(-inf)
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < k:
                return True
            while stack and stack[-1] < nums[i]:
                k = stack.pop()
            stack.append(nums[i])
            
        return False





            
        
        