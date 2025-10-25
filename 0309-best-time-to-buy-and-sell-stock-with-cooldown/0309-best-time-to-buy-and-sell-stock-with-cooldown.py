class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [0]*len(prices)
        sale = [0]*len(prices)
        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            if i > 1:
                buy[i] = max(sale[i-2]-prices[i], buy[i-1])
            else:
                buy[i] = max(-prices[i], buy[i-1])
            sale[i] = max(buy[i-1]+prices[i], sale[i-1])
        return sale[-1]
        