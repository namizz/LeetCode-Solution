class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        contain = Counter(s1)
        hashmap = defaultdict(int)
        # window size = len(s1)
        for i in range(len(s1)-1):
            hashmap[s2[i]] += 1
        for i in range(len(s1)-1,len(s2)):
            hashmap[s2[i]] += 1
            print(hashmap)
            if len(hashmap) == len(contain) and hashmap == contain:
                return True
            # print(s2[i-len(s1)+1], i, len(s1))
            hashmap[s2[i-len(s1)+1]] -= 1
            if hashmap[s2[i-len(s1)+1]] <= 0:
                hashmap.pop(s2[i-len(s1)+1])
        return False
                



        