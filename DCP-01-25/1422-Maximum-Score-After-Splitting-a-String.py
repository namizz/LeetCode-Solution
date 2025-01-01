class Solution:
    def maxScore(self, s: str) -> int:
        #split s and return the sum of left(0) and right(1)
        # we need to get maximum sum of left(0) and right(1)
        # iterate through the array count 1 and store it on right
        # left is intital 0 and iterate through the array and ifr we get 0 add it on left
        # if we get 1 subtract from right
        # ans = max(ans, right+left)
        r_sum = 0
        l_sum = 0
        ans = 0
        for num in s:
            if num == "1":
                r_sum += 1
        for num in s[:len(s)-1]:
            if num == "0":
                l_sum += 1
            else:
                r_sum -= 1
            ans = max(r_sum+l_sum, ans)
        return ans


        