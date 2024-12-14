class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # stack, hashmap
        # add if the letter in hashmap doesn't exist or if hashmap[letter] = 0 ans lenght += 1
        # slide the window left-> left+1 decrease or pop from stack from hashmap until s[left] = the letter we wanted length -= 1
        hashmap = {}
        left = 0
        length = 0
        ans = 0
        for i in range(len(s)):
            if s[i] not in hashmap or hashmap[s[i]] == 0:
                hashmap[s[i]] = 1
                length += 1
            else:
                while s[left] != s[i]:
                    hashmap[s[left]] -= 1
                    left += 1
                left += 1
                length += 1
            ans = max(ans, length - left)

        return ans

        