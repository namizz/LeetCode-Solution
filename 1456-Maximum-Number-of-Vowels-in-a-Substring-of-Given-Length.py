class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v_set = {'a','e','i','o','u'}
        vowel = 0#represent the numbeber of vowels
        for i in range(k):
            if s[i] in v_set:
                vowel += 1
        ans = vowel

        for i in range(k,len(s)):
            if s[i-k] in v_set:
                vowel -= 1
            if s[i] in v_set:
                vowel += 1
            ans = max(ans, vowel)
            if k == ans:
                break
        return ans
        