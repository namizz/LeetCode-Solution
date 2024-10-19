class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans = []
        for i in range(1, len(height)):
            if height[i-1] > threshold:
                ans.append(i)
        return ans
        