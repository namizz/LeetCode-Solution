class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = ceil(math.sqrt(c))
        contain = set()
        for i in range(n+1):
            contain.add(pow(i,2))
        for i in range(n+1):
            if c-pow(i,2) in contain:
                return True
        return False


                


