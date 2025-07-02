class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        for word in queries:
            p = 0
            b = True
            for i in word:
                if "A" <= i <= "Z":
                    if p < len(pattern) and pattern[p] == i:
                        p += 1
                    else:
                        b = False
                        break
                else:
                    if p < len(pattern) and pattern[p] == i:
                        p += 1
            if p < len(pattern):
                ans.append(False)
            else:
                ans.append(b)
        return ans
                    
        