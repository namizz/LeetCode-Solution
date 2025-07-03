class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        mask = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        for i in range(len(word)):
            mask ^= (1 << (ord(word[i])-ord("a")))
            ans += hashmap[mask]

            for j in range(10):
                ans += hashmap[mask^(1 << j)]

            hashmap[mask] += 1
        return ans

