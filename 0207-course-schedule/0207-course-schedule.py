class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # b->a
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for a,b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)
        queue = deque()
        visited = set()
        k = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                visited.add(i)
                k += 1
        while queue:
            for _ in range(len(queue)):
                x = queue.popleft()
                for i in graph[x]:
                    indegree[i] -= 1
                    if not indegree[i] and i not in visited:
                        queue.append(i)
                        visited.add(i)
                        k += 1
        return k == numCourses
