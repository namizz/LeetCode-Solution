class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        def a_func(s):
            res = [0]*len(s)
            for i in range(len(s)):
                if i%2:
                    res[i] = (int(s[i])+a)%10
                else:
                    res[i] = int(s[i])
            return "".join(map(str,res))
        def b_func(s):
            return s[-b:]+s[:len(s)-b]
        def rec(s):
            if s in visited:
                return 
            visited.add(s)
            rec(a_func(s))
            rec(b_func(s))
        rec(s)
        return min(visited)
            
            
        