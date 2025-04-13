class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hashmap = defaultdict(set)
        for a,b in trust:
            hashmap[b].add(a)
        for k in hashmap:
            if len(hashmap[k]) >= n-1:
                for k2 in hashmap:
                    if k in hashmap[k2]:
                        break
                else:
                    return k
        return -1 if n != 1 else 1
        