class Solution:
    def check(self, nums: List[int]) -> bool:
        # check from the break to the end is in non-decreasing order
        # mark the intial and go to the last by using modules of len(nums)-1
        initial = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                initial = i+1
                break
        while initial != 0 and initial < len(nums):
            print(nums[initial], nums[(initial+1)%(len(nums)-1)])
            if nums[initial] > nums[(initial+1)%(len(nums)-1)]:
                return False
            initial+=1
        return True



            

        