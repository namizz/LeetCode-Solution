class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l,r = 1,max(ranks)*(cars**2)
        def check(t):
            count = 0
            for i in range(len(ranks)):
                count += int(sqrt(t/ranks[i]))
            return count >= cars
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

        
        