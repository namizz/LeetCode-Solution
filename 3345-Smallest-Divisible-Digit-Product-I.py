class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,101):
            container = 1
            temp = i
            while temp > 0:
                container *= temp%10
                temp //=10
            if not container%t:
                return i
        

        