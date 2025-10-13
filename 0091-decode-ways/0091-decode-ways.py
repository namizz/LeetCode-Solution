class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def rec(i):
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if i in cache:
                return cache[i]
            if 1 <= int(s[i]) <= 26:
                a = rec(i+1)

            else:
                a = 0
            
            if s[i] != "0" and 1 <= int(s[i:i+2]) <= 26:
                b = rec(i+2)
            else:
                b = 0
            cache[i] = a+b
            return a + b
        return rec(0)
        