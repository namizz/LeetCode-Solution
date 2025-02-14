class Solution:
    def minimumSteps(self, s: str) -> int:
        # 10101
        # 00111
        # final ans = 000 111111
        # rp search for 0 while lp get 1
        one_c= 0
        ans = 0
        for rp in range(len(s)):
            if s[rp] == '1':
                one_c += 1
            else:
                ans += one_c
        return ans
                

        