class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        for i in range(len(hours)):
            for j in range(i+1,len(hours)):
                total = hours[i] + hours[j]
                if total >= 24 and total%24 == 0:
                    ans += 1
        return ans

        