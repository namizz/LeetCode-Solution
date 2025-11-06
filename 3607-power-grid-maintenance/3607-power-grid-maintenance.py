class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        def find(x):
            if graph[x][0] != x:
                graph[x][0] = find(graph[x][0])
            return graph[x][0]

        def union(x,y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                if rx < ry:
                    graph[ry][0] = rx
                else:
                    graph[rx][0] = ry
            
                


        graph = [[i,True] for i in range(c)]
        for a,b in connections:
            union(a-1,b-1)
        # print(graph)
    
        group = defaultdict(list)
        for i in range(len(graph)):
            a,b = graph[i]
            ra = find(a)
            heapq.heappush(group[ra], i)
        # print(group)
        online = set(i for i in range(c))
        ans = []
        for c,node in queries:
            if c == 1:
                if node-1 in online:
                    ans.append(node)
                else:
                    g = find(graph[node-1][0])
                    while group[g] and group[g][0] not in online:
                        heapq.heappop(group[g])
                    ans.append(group[g][0]+1 if group[g] else -1)
                # print(node, group)
            else:
                online.discard(node-1)
        return ans

                    
                
            
        
        

        