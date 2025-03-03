class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # c2 <= a2 + b2
        # sort in decreasing order
        # 
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0


        