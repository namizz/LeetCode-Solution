class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sale = [0]*len(prices)
        buy = [0]*len(prices)
        buy[0] = -prices[0]
        for i in range(1,len(prices)):
            buy[i] = max(buy[i-1], sale[i-1]-prices[i])
            sale[i] = max(sale[i-1], buy[i-1]+prices[i]-fee)
        return sale[-1]
        