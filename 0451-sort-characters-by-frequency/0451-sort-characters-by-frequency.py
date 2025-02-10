class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = Counter(s)
        sorted_hash = sorted(hashmap.items(), key = lambda x:x[1], reverse=True)
        ans = []
        for k, v in sorted_hash:
            while v > 0:
                ans.append(k)
                v -= 1
        return "".join(ans)
        