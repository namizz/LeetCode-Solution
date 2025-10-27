class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0
        row, col = len(bank), len(bank[0])
        for i in range(row):
            count = 0
            for j in range(col):
                if bank[i][j] == "1":
                    ans += prev
                    count += 1
            if count:
                prev = count
        return ans

                
