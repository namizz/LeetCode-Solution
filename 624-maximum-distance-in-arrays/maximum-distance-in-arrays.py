class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_d = 0
        smaller = arrays[0][0]
        bigger = arrays[0][-1]
        i = 0
        for i in range(1,len(arrays)):
            max_d = max(max_d, abs(arrays[i][-1]-smaller), abs(bigger - arrays[i][0]))
            smaller = min(arrays[i][0],smaller)
            bigger = max(arrays[i][-1], bigger)
        return max_d
        