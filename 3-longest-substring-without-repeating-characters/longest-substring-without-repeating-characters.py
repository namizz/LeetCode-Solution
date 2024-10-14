class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = deque()
        hashmap = {}
        ans = 0
        i = 0
        while i < len(s):
            if s[i] in hashmap:
                j = 0
                while j < len(window):
                    if window[j] == s[i]:
                        window.popleft()
                        break
                    hashmap.pop(window[j])
                    window.popleft()
                    
            
            window.append(s[i])
            hashmap[s[i]] = 1
            ans = max(ans, len(window))
            i += 1
        return ans
        
        