class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        queue = deque([(headID, informTime[headID])])
        ans = 0
        while queue:
            for i in range(len(queue)):
                x, t = queue.popleft()
                ans = max(t, ans)
                for des in graph[x]:
                    queue.append((des, informTime[des]+t))
        return ans
                
        
        