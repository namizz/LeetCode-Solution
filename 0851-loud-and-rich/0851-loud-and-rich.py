class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # [3,2,5,4,6,1,7,0]
        #  0 1 2 3 4 5 6 7
        # [5,5,2,5,4,5,6,7]
        
        q = {}
        for i in range(len(quiet)):
            q[i] = quiet[i]
        print(q)
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for rc,pr in richer:
            graph[rc].append(pr)
            indeg[pr] += 1
        print(graph)
        n = len(quiet)
        order = [i for i in range(n)]
        queue = deque()
        for i in range(n):
            if indeg[i] == 0:
                queue.append(i)

        while queue:
            # print(queue)
            # print(indeg)
            for _ in range(len(queue)):
                x = queue.popleft()
                for i in graph[x]:
                    indeg[i] -= 1
                    # q: order[x], q:i
                    # assign order[i] = x,i
                    if q[order[i]] > q[order[x]]:
                        order[i] = order[x]
                    if indeg[i] == 0:
                        queue.append(i)
                                              
        # print(order)
                    
        return order
        