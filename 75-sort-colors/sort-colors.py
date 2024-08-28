class Solution:
    def sortColors(self, nums: List[int]) -> None:
        lp = 0
        rp = len(nums)-1
        while lp < rp:
            if nums[lp] == 2 and nums[rp] != 2:
                print("hi",lp,rp)
                nums[lp], nums[rp] = nums[rp], nums[lp]
                lp += 1
                rp -= 1
            if nums[lp] != 2:
                lp += 1
            if nums[rp] == 2:
                rp -= 1
        lp = 0
        if nums[rp] == 2:
            rp-=1
        while lp < rp:
            if nums[lp] != 0 and nums[rp] != 1:
                nums[lp], nums[rp] = nums[rp], nums[lp]
                lp += 1
                rp -= 1
            if nums[lp] == 0:
                lp += 1
            if nums[rp] == 1:
                rp -= 1
        print(nums)