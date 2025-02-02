class Solution:
    def romanToInt(self, s: str) -> int:
        num = {'I': 1 , 'V': 5, 'X': 10, 'L': 50, 'C': 100,'D':500, 'M': 1000}
        ans = 0
        for i in range(len(s)):
            if i+1 < len(s) and num[s[i+1]] > num[s[i]]:
                ans -= num[s[i]]
            else:
                ans += num[s[i]]
        return ans



        