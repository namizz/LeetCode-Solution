class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def valid(s):
            if not s or not(0 <= int(s) < 256):
                return False
            elif len(s) > 1 and s[0] == "0":
                return False
            return True
        def backtrack(i,path):
            if i >= len(s):
                if len(path) == 4:
                    ans.append(".".join(path))
                return

            for l in range(1,4):
                if i+l > len(s):
                    break
                seg = s[i:i+l]
                if valid(seg):
                    path.append(seg)
                    backtrack(i+l, path)
                    path.pop()
            
        backtrack(0, [])
        return ans



        