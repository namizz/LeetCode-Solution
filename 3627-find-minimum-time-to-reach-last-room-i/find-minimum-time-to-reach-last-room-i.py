class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        row = len(moveTime)
        col = len(moveTime[0])
        heap = [(0,0,0)]
        visited = [[float('inf')]*col for _ in range(row)]

        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        while heap:
            time, x, y = heapq.heappop(heap)

            if(x,y) == (row-1, col-1):
                return time
            for dx, dy in direction:
                cx, cy = x+dx, y+dy
                if 0 <= cx < row and 0 <= cy < col:
                    wait_time = max(moveTime[cx][cy]-time,0)
                    new_time = time + 1 + wait_time

                    if new_time < visited[cx][cy]:
                        visited[cx][cy] = new_time
                        heapq.heappush(heap,(new_time, cx, cy))
        return -1

        