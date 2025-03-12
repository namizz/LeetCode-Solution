class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # row(4)
        # row(3)
        # row(2)
        # row(1)

        ans = [0,1,0]
        for i in range(rowIndex):
            temp = []
            temp.append(0)
            for i in range(len(ans)-1):
                temp.append(ans[i]+ans[i+1])
            temp.append(0)
            ans = temp
        return ans[1:-1]

        