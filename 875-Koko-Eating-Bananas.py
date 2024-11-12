class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hour(speed):
            time_take = sum(math.ceil(pile / speed) for pile in piles)
            return time_take
        lp ,rp = 1, max(piles)

        while lp < rp:
            mid = (lp+rp)//2
            if hour(mid) <= h:
                rp = mid 
            else:
                lp = mid + 1
        return lp

                    






        