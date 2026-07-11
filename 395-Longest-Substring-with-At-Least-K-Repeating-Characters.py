class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # valid if all string has at least k length
        # invalid if all string are less than k lenghth
        # for every index we use sliding window to check if they are valid or not
        # one hash map and one set
        # the hasmpa track the frequency of number
        # set check if the freuency of number is at least k length 
        # length of hashmap and set are the same valid
        ans = 0
        for l in range(len(s)):
            hashmap = {}
            contain = set()
            for r in range(l,len(s)):
                hashmap[s[r]] = hashmap.get(s[r],0) + 1
                if hashmap[s[r]] >= k:
                    contain.add(s[r])
                if len(hashmap) == len(contain):
                    ans = max(ans, r-l+1)
        return ans
                 

            
        