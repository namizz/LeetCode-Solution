class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # grid = [[]] size = 2*n
        # (0,0)--> move right or down
        # two robot
        # first want to minimize the point of the second robot
        # the second robot wants to maximize the number of points collect
        # return the total point collected by robot2
        # we are gonna use prefix sum
        # ```````````````````````````````````````````````
        # we need the maximum way from (0,0)->(1,n-1) 
        # make the path grid[r][c]=0
        # find a maximum path from(0,0)->(1,n-1) return the total sum
        # ```````````````````````````````````````````````
        # we need two array with []*n
        # store the prefix sum from back to front
        # when we get index which to go to down
        # another for loop to calculate prefix sum
        # track the maximum
        n = len(grid[0])
        top = grid[0][:]
        bottom = grid[1][:]
        for i in range(n-1):
            top[i+1] += top[i]
        for i in range(n-1,0,-1):
            bottom[i-1] += bottom[i]
        ans = float(inf)
        for i in range(n):
            temp = max(top[n-1]-top[i], (bottom[0]-bottom[i] if i > 0 else 0))
            ans = min(temp, ans)       
        return ans  
            


      
