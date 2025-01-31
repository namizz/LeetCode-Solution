class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # rowSum = [], colSum = []
        # return originalArr
        # [3, 0] = 0 
        # [1, 7] = 8
        #  1  7
        """[1,5,0]=0,
           [7,0,0]=0,
           [0,0,10]=10"""
        #   0 0 10
        # our goal to to make all rowSum and ColSum to be 0,0,0
        # find the min from rowSum
        # find the min from colSum
        # replace it with the [r][c] subtract from rowSum and ColSum
        ans = []
        for i in range(len(rowSum)):
            ans.append([0]*len(colSum))
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                temp = min(rowSum[i], colSum[j])
                ans[i][j] = temp
                rowSum[i] -= temp
                colSum[j] -= temp
        return ans

        

        