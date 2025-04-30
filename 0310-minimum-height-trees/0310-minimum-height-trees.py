class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        indeg = [0]*n
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indeg[a] += 1
            indeg[b] += 1
        print(graph)
        print(indeg)
        queue = deque()
        for i in range(len(indeg)):
            if indeg[i] == 1:
                queue.append(i)
        visited = set()
        left = n
        while queue:
            ans = []
            # print(queue)
            left -= len(queue)
            for i in range(len(queue)):
                x = queue.popleft()
                ans.append(x)
                visited.add(x)
                indeg[x] -= 1
                for i in graph[x]:
                    if i not in visited:
                        indeg[i] -= 1
                        if indeg[i] == 1:
                            queue.append(i)
        return ans


        