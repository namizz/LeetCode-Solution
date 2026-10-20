class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        count = 0
        ans = [-1] * (len(s)+1)
        for i in range(len(s)):
            if s[i] == 'I':
                ans[i] = count
                count += 1
                if i == len(s)-1:
                    ans[i+1] = count
                    count += 1

        for i in range(len(s)-1,-1,-1):
            if s[i] == 'D':
                if i == len(s)-1:
                    ans[i+1] = count
                    count += 1
                ans[i] = count
                count += 1
        return ans
        