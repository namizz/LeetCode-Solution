class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        #s:string
        #we need subsquence string with a length 3
        #return number unique palindome of length three
        ans = set()
        left = set()
        right= Counter(s)
        for mid in s:
            right[mid] -= 1
            if right[mid] == 0:
                right.pop(mid)
            for j in range(26):
                c = chr(ord('a')+j)
                if c in left and c in right:
                    ans.add((mid, c))
            left.add(mid)
        return len(ans)
                

        