class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        ingroup = set()
        ans = 0
        for r in range(len(isConnected)):
            if r not in ingroup:
                for c in range(len(isConnected[0])):
                    if isConnected[r][c]:
                        ingroup.add(c)
                ans += 1
        return ans


        