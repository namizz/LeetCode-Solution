class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def check(i, k):
            return (i*(i-1)) == k
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        ans = 0
        for i in range(n):
            if i not in visited:
                queue = deque([i])
                visited.add(i)
                node = {i}
                k = 0
                while queue:
                    x = queue.popleft()
                    for des in graph[x]:
                        k += 1
                        if des not in visited:
                            queue.append(des)
                            visited.add(des)
                            node.add(des)
                if check(len(node), k):
                    ans += 1
        return ans






        