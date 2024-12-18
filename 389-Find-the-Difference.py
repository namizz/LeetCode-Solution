class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap = Counter(s)
        for i in t:
            if hashmap[i] == 0:
                return i
            hashmap[i]-=1
        