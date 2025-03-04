class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        # move from 1-> target
        # target: int, maxDouble:int
        # maxDouble-> number of times that you can move in 2*your position
        # target = 19, maxDouble = 2
        # add remider on ans = 1/0
        # add 1 when we use maxDouble
        # rest will be add on ans
        # 10 2
        # 1 ans = 4
        ans = 0
        while maxDoubles > 0 and target > 1:
            q = target//2
            r = target%2
            ans += (r + 1)
            maxDoubles -= 1
            target //=2
        ans +=  target
        return ans-1


        