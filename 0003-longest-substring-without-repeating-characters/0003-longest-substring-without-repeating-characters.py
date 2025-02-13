class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contain = set()
        p = 0
        ans = 0
        for i in range(len(s)):
            if s[i] not in contain:
                contain.add(s[i])
            else:    
                ans = max(ans, len(contain))
                while s[p] != s[i]:
                    contain.remove(s[p])
                    p += 1
                p += 1
        return max(ans, len(contain))
            
        