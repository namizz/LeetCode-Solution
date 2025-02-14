class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # window size should be minimum we need t in the s
        # we can decrese the size of the window if we get the duplicate
        # window start with element in t
        if len(s) < len(t):
            return ""

        contain =defaultdict(int)
        for c in t:
            contain[c] += 1
        def is_valid(win, con):
            for c in con:
                if con[c] > win[c]:
                    return False
            return True

        window = defaultdict(int)
        j = 0
        ans = [-1,-1]
        shortest = float('inf')
        for i in range(len(s)):
            window[s[i]] += 1  
            while is_valid(window, contain):
                if i-j+1 < shortest:
                    shortest = i - j + 1
                    ans = [j, i]

                window[s[j]] -= 1
                j += 1


        if ans[0] == -1:
            return ""
        return s[ans[0]:ans[1]+1]
        
                

        