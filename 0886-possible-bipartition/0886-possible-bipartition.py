class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(idx, color):
            if visited[idx] != -1:
                return visited[idx] == color

            visited[idx] = color

            for i in hashmap[idx]:
                if not dfs(i, 1-color):
                    return False  
            return True          
        hashmap = defaultdict(list)
        for a,b in dislikes:
            hashmap[a].append(b)
            hashmap[b].append(a)
        visited = [-1] * (n + 1)
        for i in range(1, n+1):
            if visited[i] == -1:
                if not dfs(i, 0):
                    return False
        return True


            

        