class Solution:
    def mySqrt(self, x: int) -> int:
        lp, rp = 0,x
        while lp <= rp:
            mid = (lp+rp)//2
            nums = mid*mid
            if nums <= x:
                lp = mid + 1
            else:
                rp = mid - 1
        return rp


        