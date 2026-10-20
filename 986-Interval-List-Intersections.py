class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        i,j = 0,0
        ans = []
        while i < len(firstList) and j < len(secondList):
            si,ei = firstList[i]
            sj, ej = secondList[j]

            if ei > ej:
                if ej >= si:
                    ans.append([max(si,sj), ej])
                j += 1
            else:
                if ei >= sj:
                    ans.append([max(si,sj), ei])
                i += 1
        return ans

        