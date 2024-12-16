class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = Counter(s)
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1

        