class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ev = defaultdict(dict)
        visited = set()
        def dfs(x, y,visit):
            if x not in ev or y not in ev:
                return -1
            if y in ev[x]:
                return ev[x][y]
            for i in ev[x]:
                if i not in visit:
                    visit.add(i)
                    temp = dfs(i,y,visit)
                    if temp != -1:
                        return ev[x][i]*temp                       
                    
            return -1
            


        for i in range(len(equations)):
            x,y = equations[i]
            val = values[i]
            ev[x][y] = val
            ev[y][x] = 1/val
        print(ev)
        ans = []
        for x,y in queries:
            ans.append(dfs(x,y,set()))
        return ans

        
        