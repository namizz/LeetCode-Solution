class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        c1 = 1
        c2 = 1
        dec = 0
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i] and not dec:
                c1 += 1
            elif nums[i-1] < nums[i] and dec:
                c2 += 1
            elif not dec and c1 >= k:
                dec += 1
            else:
                c1 = 1
                c2 = 1
                dec = 0
            if (c1 >= k and c2 >= k) or c1 >= 2*k:
                return True
        return False




        