class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # matrix = [[]]
        # return spiral print
        # we need inward moving row and col we decrease the number of row&col
        # we need a postion
        # we need if we are moving forward or downward or backward or upward
        # make a method that takes position, number of rows to iterate, end point, the direction
        # for forward, end point be like pos to pos->row
        # for backward, end point be like pos to len(pos)->pos backward
        # def move(iterable,constant,left,direction):
        #     for i in range(iterable, left):
        #         ans.append(matrix[constant][i])
        ans = [] 
        t,b = 0, len(matrix)-1
        l,r = 0, len(matrix[0])-1
        while t <= b and l <= r:
            for j in range(l,r+1):
                ans.append(matrix[t][j])
            t += 1
            for i in range(t,b+1):
                ans.append(matrix[i][r])
            r -= 1
            if t <= b:
                for j in range(r,l-1,-1):
                    ans.append(matrix[b][j])
                b -= 1
            if l <= r:
                for i in range(b,t-1,-1):
                    ans.append(matrix[i][l])
                l += 1
        return ans


            
        