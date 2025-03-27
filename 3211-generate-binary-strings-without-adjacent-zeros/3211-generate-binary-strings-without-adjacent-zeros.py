class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def back(path):
            if len(path) == n:
                ans.append("".join(path))
                return
            back(path+['0'])
            back(path+['1'])
        back([])
        res = []
        for i in ans:
            if "00" not in i:
                res.append(i)
        return res
        