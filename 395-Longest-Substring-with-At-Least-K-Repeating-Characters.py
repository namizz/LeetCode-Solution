class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for t in range(1,27):
            hashmap = {}
            l = 0
            d = 0
            c = 0
            for r in range(len(s)):
                if s[r] not in hashmap:
                    d += 1
                hashmap[s[r]] = hashmap.get(s[r],0) + 1

                if hashmap[s[r]] == k:
                    c += 1

                while d > t:
                    if hashmap[s[l]] == k:
                        c -= 1
                    hashmap[s[l]] -= 1
                    if not hashmap[s[l]]:
                        d -= 1
                        del hashmap[s[l]]
                    l += 1
                if d == t and c == t:
                    ans = max(ans, r-l+1)
        return ans
                
                


                 

            
        