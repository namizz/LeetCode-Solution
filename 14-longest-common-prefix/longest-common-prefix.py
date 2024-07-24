class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        pos = 0
        while pos < len(strs[0]):
            k = 0
            while k < len(strs):
                if pos >= len(strs[k]) or strs[0][pos] != strs[k][pos]:
                    return "".join(ans)
                k += 1
            ans.append(strs[0][pos])
            pos += 1
        return "".join(ans)


                

                

        