class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def operation(x):
            ans = []
            ans.append(x)
            ans.append("1")
            for i in range(len(x)-1,-1,-1):
                if x[i] == "0":
                    ans.append("1")
                else:
                    ans.append("0")
            return "".join(ans)
        def recurion(n):
            if n == 1:
                return "0"
            return operation(recurion(n-1))
        return recurion(n)[k-1]