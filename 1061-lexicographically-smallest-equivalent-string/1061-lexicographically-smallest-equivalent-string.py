class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        hashmap = defaultdict(str)
        def find(x):
            if hashmap[x] != x:
                hashmap[x] = find(hashmap[x])
            return hashmap[x]
        def union(x,y):
            rx, ry = find(x), find(y)
            if rx > ry:
                hashmap[rx] = ry
            else:
                hashmap[ry] = rx
        for i in range(26):
            l = chr(97+i)
            hashmap[l] = l
        for i in range(len(s1)):
            union(s1[i],s2[i])
        ans = []
        for s in baseStr:
            ans.append(find(s))
        return "".join(ans)


        
        
        