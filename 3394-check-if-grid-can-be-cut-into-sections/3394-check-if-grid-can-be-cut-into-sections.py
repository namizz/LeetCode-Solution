class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(r, d):
            gap = 0
            r.sort(key=lambda x:x[d])
            end = r[0][d+2]
            for i in range(1,len(r)):
                rec = r[i]
                if end <= rec[d]:
                    gap += 1
                end = max(end, rec[d+2])
            return gap >= 2
        return check(rectangles,0) or check(rectangles,1)
        


        