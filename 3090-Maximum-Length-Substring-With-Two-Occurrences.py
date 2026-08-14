class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        hashmap = {}
        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            while hashmap[s[right]] > 2:
                hashmap[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return max(len(s) - left, ans)



        