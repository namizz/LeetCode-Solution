class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        for i in range(1,len(word)):
            if word[i-1] == word[i]:
                ans += 1
        return ans

        