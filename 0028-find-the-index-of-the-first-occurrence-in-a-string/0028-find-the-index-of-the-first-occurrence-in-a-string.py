class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if needle == haystack:
            return 0
        for i in range(len(needle), len(haystack)+1):
            if needle == haystack[i-len(needle):i]:
                return i-len(needle)
        return -1
        