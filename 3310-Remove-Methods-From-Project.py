class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        hashmap = defaultdict(list)
        visited = [False] * n
        for a,b in invocations:
            hashmap[a].append(b)
        
        def recursive(k):
            visited[k] = True
            for a in hashmap[k]:
                if not visited[a]:
                    recursive(a)
        recursive(k)

        for u, v in invocations:
            if not visited[u] and visited[v]:
                return [i for i in range(n)]
        ans = []
        for i in range(n):
            if not visited[i]:
                ans.append(i)
        return ans
            
                

        
        
            
        