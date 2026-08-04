class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # 5,  5
        # 3,  5   5,4
        # -1,1 -1,1 -1,1  2,-2
        cache = {}
        def rec(start,end, alice):
            if start > end:
                return 0
            if (start, end) in cache:
                return cache[(start,end)]
            result = 0
            if alice:
                result = max( piles[start] + rec(start+1, end, not alice), piles[end] + rec(start, end-1, not alice))
            else:
                result = min(rec(start+1,end, not alice)-piles[start], rec(start, end-1, not alice)-piles[end])
            cache[(start,end)] = result
            return result
        k = rec(0, len(piles)-1, True)
        return True if k > 0 else False

        
            
        