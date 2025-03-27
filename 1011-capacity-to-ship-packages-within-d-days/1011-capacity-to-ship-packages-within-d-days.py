class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        def check(x):
            d = 1
            contain = 0
            for weg in weights:
                if contain + weg <= x:
                    contain += weg
                else:
                    d += 1
                    contain = weg
            return d <= days   
        
        ans = 0
        while l <= r:
            mid = (l + r)//2
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans



        