class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        arr = [True]*n
        arr[0] = arr[1] = False

        p = 2
        while p*p < n:
            if arr[p]:
                for i in range(p*p, n, p):
                    arr[i] = False                

            p += 1
        return sum(arr)

        