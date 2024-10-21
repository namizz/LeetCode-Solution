class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        j = 0
        max_v = 0
        ans = 0
        i = 0
        while i < len(s):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
            max_v = max(max_v, hashmap[s[i]])
            if (i - j +1) - max_v > k:
                hashmap[s[j]] -= 1
                j += 1
            
            ans = max(i-j+1, ans)
            i += 1
        return ans


        