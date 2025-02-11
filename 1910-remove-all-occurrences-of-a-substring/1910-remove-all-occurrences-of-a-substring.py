class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # remove the part from s
        ans = []
        np = 1-len(part)
        list_part = list(part[:len(part)-1])
        for i in range(len(s)):
            if s[i] == part[-1] and ans[np:] == list_part:
                deleted = len(list_part)
                while deleted > 0:
                    ans.pop()
                    deleted -= 1
            elif s[i] == part[-1] and len(list_part) == 0:
                continue
            else:
                ans.append(s[i])
        return "".join(ans)
                



        