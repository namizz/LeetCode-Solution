class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indeg = defaultdict(int)
        hashmap = defaultdict(list)

        for i in range(len(graph)):
            for j in graph[i]:
                hashmap[j].append(i)
                indeg[i] += 1
        # print(hashmap)
        # print(indeg)
        queue = deque()
        for i in range(len(graph)):
            if not indeg[i]:
                queue.append(i)
        # print(queue)

        ans = []
        while queue:
            n = queue.popleft()
            ans.append(n)
            for i in hashmap[n]:
                indeg[i] -= 1
                if not indeg[i]:
                    queue.append(i)
                
                
        return sorted(ans)



       
