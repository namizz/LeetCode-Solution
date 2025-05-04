class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashmap = defaultdict(list)
        for i in range(len(dominoes)):
            a,b = dominoes[i]
            hashmap[a+b].append(i)
        ans = 0
        for _,ll in hashmap.items():
            for i in range(len(ll)):
                a,b = dominoes[ll[i]]
                for j in range(i+1, len(ll)):
                    c,d = dominoes[ll[j]]
                    if (a == d and b == c )or( a == c and b == d):
                        ans += 1
        return ans



        return ans

        