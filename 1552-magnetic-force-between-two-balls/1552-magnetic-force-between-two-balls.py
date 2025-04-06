class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # minimum force to be maximum
        # minimum can be 0
        # maximum = max(position)
        # 1,2,4,100  --- 3
        # ans = 3
        def check(x):
            balls = 1
            temp = position[0]
            for i in range(len(position)):
                if position[i]-temp >= x:
                    balls += 1
                    temp = position[i]
            return balls >= m



        position.sort()
        l,r = 0, position[-1]
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
        