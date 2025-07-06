class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [i for i in range(n)]
        def find(x):
            if graph[x] != x:
                graph[x] = find(graph[x])
            return graph[x]
        def union(x,y):
            rx, ry = find(x), find(y)
            if rx != ry:
                graph[ry] = rx
        i = 0
        edgeList.sort(key=lambda x:x[2])
        que = [(p, q, limit, idx) for idx, (p, q, limit) in enumerate(queries)]
        que.sort(key=lambda x: x[2])
        ans = [False] * len(queries)
        for p,q,limit,idx in que:
            while i < len(edgeList) and edgeList[i][2] < limit:
                x,y,l = edgeList[i]
                union(x,y)
                i += 1 
            ans[idx] = find(p) == find(q)
        return ans

        