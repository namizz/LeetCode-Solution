class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        del_col = 0
        for i in range(len(strs[0])):
            for j in range(len(strs) - 1):
                if strs[j][i] > strs[j + 1][i]:
                    del_col += 1
                    break
        return del_col


        