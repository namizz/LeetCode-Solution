class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # color 0=white and 1=black and -1=no-color
        # start from 0 and color all the adjecents it's opposite color
        colors = [-1]*len(graph)
        prev = 0
        for c in range(len(colors)):
            if colors[c] == -1:
                colors[c] = prev%2
                queue = deque(graph[c])
                while queue:
                    prev += 1
                    for i in range(len(queue)):
                        x = queue.popleft()
                        if colors[x] == -1:
                            colors[x] = prev%2
                            queue.extend(graph[x])
                        elif colors[x] != prev%2:
                            return False                
        # print(colors)
        # for c in colors:
        #     if c == -1:
        #         return False
        return True 

        
        