class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        contain = set()
        l = 0
        ans = float('inf')
        for r in range(len(cards)):
            while cards[r] in contain:
                ans = min(r-l+1,ans)
                contain.remove(cards[l])
                l += 1
            contain.add(cards[r])
        return -1 if ans == float(inf) else ans
         
            

        