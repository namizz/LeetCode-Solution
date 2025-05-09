class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        hashmap = {}
        def find(x):
            if hashmap[x] != x:
                hashmap[x] = find(hashmap[x])
            return hashmap[x]
        
        # Union
        def union(x, y):
            hashmap[find(x)] = find(y)
        
        ep = {}
        for i in range(len(accounts)):
            name = accounts[i][0]
            for e in accounts[i][1:]:
                if e not in hashmap:
                    hashmap[e] = e
                ep[e] = name
                union(accounts[i][1], e)
 
        u = defaultdict(list)
        for i in hashmap:
            root = find(i)
            u[root].append(i)
        ans = []
        for i in u:
            ans.append([ep[i]]+ sorted(u[i]))
        return ans

