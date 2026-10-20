class Solution:
    def maxArea(self, height: list[int]) -> int:
        # area = l * w
        # question to maximize l and width
        # we can't add l but choose
        # width determined on length we are going to choose
        # 
        l = 0
        r = len(height)-1
        ans = 0
        while l < r:
            w = r-l 
            h = min(height[l], height[r])
            ans = max(ans, h*w)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return ans 

        