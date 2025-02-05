class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashmap = Counter(s)
        if len(s)%len(hashmap) != 0:
            return False
        for v in hashmap.values():
            if v != len(s)//len(hashmap):
                return False
        return True
        