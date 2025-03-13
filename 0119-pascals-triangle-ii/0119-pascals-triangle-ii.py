class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # row(4)
        # row(3)
        # row(2)
        # row(1)
        def operation(x):
            temp = []
            temp.append(1)
            for i in range(len(x)-1):
                temp.append(x[i]+x[i+1])
            temp.append(1)
            return temp
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        ans = operation(self.getRow(rowIndex-1))
        
        return ans
        