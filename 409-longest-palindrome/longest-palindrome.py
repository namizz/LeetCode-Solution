class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter = set()
        for i in range(len(s)):
            if s[i] not in letter:
                letter.add(s[i])
            elif s[i] in letter:
                letter.remove(s[i])
        return len(s) - len(letter) + 1 if letter else len(s)
        