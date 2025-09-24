class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        ans = float(inf)
        cache = {}
        def dp(n):
            if n == 0:
                return 0
            if n < 0:
                return float('inf')
            if n in cache:
                return cache[n]
            cache[n] = min(1+dp(n-i) for i in coins)
            return cache[n]
        ans = dp(amount)
        return ans if ans != float(inf) else -1 
            
            

        