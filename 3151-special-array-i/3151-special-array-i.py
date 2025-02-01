class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        odd = False if nums[0]%2 == 0 else True
        for i in nums:
            if odd and i%2 != 1:
                return False
            elif not odd and i%2 != 0:
                return False
            else:
                odd= not odd
        return True


        