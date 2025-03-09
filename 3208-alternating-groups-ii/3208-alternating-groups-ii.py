class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        c = colors+colors
        same = 0
        ans = 0
        for i in range(1,k):
            if colors[i] == colors[i-1]:
                same += 1
        for i in range(k, len(colors)+k):
            if same == 0:
                ans += 1
            if c[i] == c[i-1]:
                same += 1
            if c[i-k] == c[i-k+1]:
                same -= 1
        return ans




        