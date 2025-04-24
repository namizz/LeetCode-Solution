class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indeg = defaultdict(int)
        graph = defaultdict(list)

        for fm,to in edges:
            graph[fm].append(to)
            indeg[to] += 1
        queue = deque()

        for i in range(n):
            if indeg[i] == 0:
                queue.append(i)
        ans = [set() for i in range(n)]
        while queue:
            for i in range(len(queue)):
                x = queue.popleft()
                for i in graph[x]:
                    indeg[i] -= 1
                    ans[i].update(ans[x])
                    ans[i].add(x)
                    if indeg[i] == 0:
                        queue.append(i)
        for i in range(n):
            ans[i] = sorted(list(ans[i]))
        return ans
        
            
        