class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        #sort 0
        lp = 0
        for rp in range(1,len(nums)):
            if nums[lp] > nums[rp]:
                nums[lp], nums[rp] = nums[rp], nums[lp]
            while nums[lp] == 0 and lp < rp:
                lp += 1
        # sort 1
        for rp in range(lp, len(nums)):
            if nums[lp] > nums[rp]:
                nums[lp], nums[rp] = nums[rp], nums[lp]
            while nums[lp] == 1 and lp < rp:
                lp += 1


        