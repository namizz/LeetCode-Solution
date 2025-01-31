class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            quotient = numBottles//numExchange
            ans += quotient
            numBottles = numBottles%numExchange + quotient
        return ans
        