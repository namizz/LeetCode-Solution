class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        for i in range(len(grid)):
            h = nlargest(limits[i], grid[i])
            heap.extend(h)
        return sum(nlargest(k,heap))

                    
        