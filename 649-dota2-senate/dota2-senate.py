class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D = deque()
        R = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == 'R':
                R.append(i)
            else:
                D.append(i)
        print(R,D)
        while D and R:
            if D[0] < R[0]:
                D.popleft()
                R.popleft()
                D.append(n)
            else:
                D.popleft()
                R.popleft()
                R.append(n)
            n += 1
        return "Dire" if D else "Radiant"

        