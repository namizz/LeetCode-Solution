class Solution:
    def maxScore(self, s: str) -> int:
        #split s and return the sum of left(0) and right(1)
        # we need to get maximum sum of left(0) and right(1)
        # iterate through the array count 1 and store it on right
        # left is intital 0 and iterate through the array and ifr we get 0 add it on left
        # if we get 1 subtract from right
        # ans = max(ans, right+left)
        right = 0
        left = 0
        for i in s:
            if i == "1":
                right += 1
        ans = 0
        for i in s[:len(s)-1]:
            if i == "1":
                right -= 1
            else:
                left += 1
            ans = max(ans, left+right)
        return ans

        