class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]: 
        red = {}
        blue = {}
        for i in range(n):
            red[i] = []
            blue[i] = []
        for a,b in redEdges:
            red[a].append(b)
        for a,b in blueEdges:
            blue[a].append(b)

        queue = deque([(0,0)])
        ans = [-1]*n
        visited = set()
        rv = set()
        bv = set()
        while queue:
            for _ in range(len(queue)):
                x, val = queue.popleft()
                if ans[x] != -1:
                    ans[x] = min(val, ans[x])
                else:
                    ans[x] = val
                if not val%2: 
                    bv.add(x)
                    for i in red[x]:
                        if i not in rv:
                            queue.append((i,val+1))
                else:
                    rv.add(x)
                    for i in blue[x]:
                        if i not in bv:
                            queue.append((i,val+1))

        bv, rv = set(), set()
        queue = deque([(0,0)])
        while queue:
            for _ in range(len(queue)):
                x, val = queue.popleft()
                if ans[x] != -1:
                    ans[x] = min(val, ans[x])
                else:
                    ans[x] = val
                if val%2: 
                    bv.add(x)
                    for i in red[x]:
                        if i not in rv:
                            queue.append((i,val+1))
                else:
                    rv.add(x)
                    for i in blue[x]:
                        if i not in bv:
                            queue.append((i,val+1))
        # print(ans)
        return ans
                

        