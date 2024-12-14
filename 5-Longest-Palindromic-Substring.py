class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s: string, 
        #return longest palindromic substring
        # brute force: o(n3)
        # loop from 1-last
        # two pointer take sub array 
        # check if they are a palindrome 
        # what would be the effecient solution?
        # for palindrome string their must be n number of char for n%2==0/\\1
        # iterate through the array an when we get the duplicate value check if that sub-string is a palindrom
        start, end = 0,0
        def check_palindrome(lp,rp):
            while lp >= 0 and rp < len(s) and s[lp] == s[rp]:
                lp -= 1
                rp += 1
            return lp + 1, rp
        for i in range(len(s)):
            lo, ro = check_palindrome(i,i)
            le, re = check_palindrome(i,i+1)

            if ro-lo > end-start:
                start, end = lo, ro
            if re-le > end-start:
                start, end = le, re
        return s[start:end]




        