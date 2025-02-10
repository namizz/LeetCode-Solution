class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # limit = int,  queries = [[]]
        # number of colors used, the len(hashmap)
        # {ball: color used}
        # {color : frequency}
        ball = {}
        color = defaultdict(int)
        ans = []
        for b, c in queries:
            color[c] += 1
            if b not in ball:
                ball[b] = c
            else:
                color[ball[b]] -= 1 
                if color[ball[b]] == 0:
                    color.pop(ball[b])
                ball[b] = c
            ans.append(len(color))
        return ans
            
