class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t,b = 0,len(matrix)-1
        l,r = 0, len(matrix[0])-1
        ans = 0
        while t <= b:
            mid = (t+b)//2
            if matrix[mid][l] <= target:
                ans = mid
                t = mid+1
            else:
                b = mid-1
        side = 0
        while l <= r:
            mid = (l+r)//2
            if matrix[ans][mid] < target:
                l = mid + 1
            elif matrix[ans][mid] > target:
                r = mid -1 
            else:
                return True
        return False
                
            






        