class Solution:
    def minimumLength(self, s: str) -> int:
        #s:string
        #return minlength of string
        # string is filtered
        # choose i in s[i] have similar value in left, right
        hashmap = Counter(s)
        ans = 0
        for i in hashmap:
            if hashmap[i] > 2:
                if hashmap[i]%2 == 0:
                    hashmap[i] = 2
                else:
                    hashmap[i] = 1
            ans += hashmap[i]
        return ans
            
        