class Solution:
    def findRedundantConnection(self, edges):
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)
        def find(x):
            x = par[x]
            while x != par[x]:
                par[x] = par[par[x]]
                x = par[x]
            return x
        def unioin(x,y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True
        for a,b in edges:
            if not unioin(a,b):
                return [a,b]
        
        
            
