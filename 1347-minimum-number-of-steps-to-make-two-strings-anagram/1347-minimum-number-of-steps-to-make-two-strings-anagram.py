class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashmap = Counter(s)
        count = 0
        for i in range(len(t)):
            if t[i] in hashmap:
                hashmap[t[i]] -= 1
            else:
                hashmap[t[i]] = 1
        for v in hashmap.values():
            count += abs(v)
        return count//2
                
        