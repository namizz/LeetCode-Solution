class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        hashmap = defaultdict(list)
        for a,b in edges:
            hashmap[a].append(b)
            if b not in hashmap:
                hashmap[b] = []

        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for i in hashmap[node]:
                dfs(i)

            


        visited = set()
        print(hashmap)
        for node in hashmap:
            if node not in visited:
                visited = set()
                for i in hashmap[node]:
                    dfs(i)
                if len(visited)+1 == n:
                    return node
        return -1 if n != 1 else 0




        