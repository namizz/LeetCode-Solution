class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        rp = ceil(math.sqrt(c))
        lp = 0
        while lp <= rp:
            x = pow(lp,2)
            y = pow(rp,2)
            if x+y > c:
                rp -= 1
            elif x+y < c:
                lp += 1
            else:
                return True
        return False


                


