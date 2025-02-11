class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # remove the part from s
        ans = []
        np = 1-len(part)
        list_part = list(part[:len(part)-1])
        print(list_part)
        for i in range(len(s)):
            print(ans[np:], i)
            if s[i] == part[-1] and ans[np:] == list_part:
                deleted = len(list_part)
                while deleted > 0:
                    ans.pop()
                    deleted -= 1
            else:
                ans.append(s[i])
        return "".join(ans)
                



        