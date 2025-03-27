class Solution:
    def punishmentNumber(self, n: int) -> int:
        total = 0
        def back(idx, path, sq):
            nonlocal total
            if idx >= len(sq):
                k = sum(map(int, path))
                if k == int(sq)**0.5:
                    total += int(sq)
                return
            back(idx+1, path+[sq[idx]], sq)
            if path:
                path[-1] += sq[idx]
                back(idx+1, path, sq)
        for i in range(1,n+1):
            back(0,[], str(i*i))
        return total
        