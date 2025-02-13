from typing import List



class Solution:
    def maxArea(self, height: List[int]) -> int:

        max1 = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                max1 = max(max1, height[i] * (j - i))
                i += 1
            else:
                max1 = max(max1, height[j] * (j - i))
                j -= 1

        return max1


height = [1,8,6,2,5,4,8,3,7]
p = Solution()
print(p.maxArea(height))

