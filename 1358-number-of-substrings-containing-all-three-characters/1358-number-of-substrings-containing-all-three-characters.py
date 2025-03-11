class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        j = 0
        ans = 0
        hashmap = defaultdict(int)
        for i in range(len(s)):
            hashmap[s[i]] += 1
            while len(hashmap) == 3:
                hashmap[s[j]] -= 1
                if hashmap[s[j]] == 0:
                    hashmap.pop(s[j])
                j += 1
            ans += j
        return ans
            



        