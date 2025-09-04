class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def value(curr):
            if curr == 0:
                return 0,0
            elif curr == 1:
                return 1, 0
            elif curr == 2:
                return 0, 1
            else:
                return 1,1

        interate = max(len(a), len(b))
        ans = [0]*(interate + 1)
        rem = 0
        for i in range(1,interate+1):
            curr = 0
            if i <= len(a) and a[-i] == "1":
                curr += 1
            if i <= len(b) and b[-i] == "1":
                curr += 1
            if rem:
                curr += 1
            add, rem = value(curr)
            ans[-i] += add
        if rem:
            ans[0] += 1
            return "".join(map(str, ans))
            
        return "".join(map(str,ans[1:]))
            
            
        