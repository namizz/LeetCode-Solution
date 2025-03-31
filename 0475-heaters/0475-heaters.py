class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # 1 3 5 6 7 8 9 11 15
        # *         |       *
        l = 0
        ans = 0
        for i in range(len(houses)):
            if l < len(heaters)-1 and abs(houses[i]-heaters[l]) >= abs(houses[i]-heaters[l+1]):
                l += 1
            ans = max(ans, abs(houses[i]-heaters[l]))


        return ans


                


        