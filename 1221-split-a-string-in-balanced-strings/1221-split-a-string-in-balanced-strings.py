class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R = 0
        L = 0
        ans = 0
        for l in s:
            if l == "R":
                R += 1
            else:
                L += 1
            if R == L:
                ans += 1

        return ans
        