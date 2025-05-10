class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        def union(x,y):
            px, py = find(x), find(y)
            if px != py:
                root[py]= px

        hashmap = {}
        root = []
        for s in equations:
            a, b = s[0], s[-1]
            if a not in hashmap:
                x = len(hashmap)
                hashmap[a] = x
                root.append(x)
            if b not in hashmap:
                y = len(hashmap)
                hashmap[b] = y
                root.append(y)
        for s in equations:
            eq = s[1:-1]
            if eq == "==":
                a, b = hashmap[s[0]], hashmap[s[-1]]
                ans = union(a,b)
        # print(hashmap)
        # print(root)
        for s in equations:
            a, b = s[0],s[-1]
            eq = s[1:-1]
            if eq == "!=" and find(hashmap[a]) == find(hashmap[b]):
                return False
        return True
            



        