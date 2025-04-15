class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        ingroup = set()
        ans = 0
        for r in range(len(isConnected)):
            if r not in ingroup:
                queue = deque([r])
                while queue:
                    x = queue.popleft()
                    for c in range(len(isConnected[0])):
                        if isConnected[x][c] and c not in ingroup:
                            ingroup.add(c)
                            queue.append(c)
                ans += 1
        return ans


        