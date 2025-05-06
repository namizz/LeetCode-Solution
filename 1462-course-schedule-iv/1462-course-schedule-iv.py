class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # numCourse: int, prerequisites= [[]], queries = [[]]
        # true if queries[j] =[ui, vi] where ui is prerequsite for vi
        
        graph = defaultdict(set)
        indeg = defaultdict(int)
        for a,b in prerequisites:
            graph[a].add(b)
            indeg[b] += 1
        # indirect relation
        queue = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)

        ans = defaultdict(set)
        while queue:
            for i in range(len(queue)):
                x = queue.popleft()
                for i in graph[x]:
                    ans[i].add(x)
                    ans[i].update(ans[x])
                    indeg[i] -= 1
                    if indeg[i] == 0:
                        queue.append(i)
        # print(ans)
        result = []
        for ui,vi in queries:
            result.append(ui in ans[vi])
        return result
             