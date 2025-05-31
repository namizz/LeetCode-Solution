class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        queue = deque([(headID, informTime[headID])])
        ans = 0
        while queue:
            time = 0
            for i in range(len(queue)):
                x, t = queue.popleft()
                time = max(t, time)
                for des in graph[x]:
                    queue.append((des, informTime[des]+t))
            ans = max(time, ans)
        return ans
                
        
        