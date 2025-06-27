class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # goal: to make the graph to be traverse through alice and bob
        # return int: number_removable
        # return -1: alice or bob can travese through at least one node
        # Alice Graph:- contain edges that belongs to Alice 
        # Bob Graph:- contains edge that belong to Bob
        # ignore repetable edges and edges that connects with same root node
        Alice = [i for i in range(n+1)]
        Bob = [i for i in range(n+1)]
        edges.sort(key=lambda x:x[0], reverse=True)
        def find(graph, x):
            if x != graph[x]:
                graph[x] = find(graph,graph[x])
            return graph[x]
        ans = 0 # answer would be the removable edges
        def union(graph, x, y):
            rootx = find(graph, x)
            rooty = find(graph, y)
            if rootx != rooty:
                graph[rooty] = rootx
                return True
            return False
        for t,u,v in edges:
            if t == 1:
                if not union(Alice, u,v):
                    ans += 1
            elif t == 2:
                if not union(Bob, u,v):
                    ans += 1
            else:
                k = union(Alice, u, v) 
                l = union(Bob, u, v)
                if not(k and l):
                    ans += 1
   
        rootAlice = set()
        rootBob = set()
        for i in range(1, n+1):
            rootAlice.add(find(Alice,i))
            rootBob.add(find(Bob,i))

        return ans if len(rootAlice)+len(rootBob) == 2 else -1
            


        

        