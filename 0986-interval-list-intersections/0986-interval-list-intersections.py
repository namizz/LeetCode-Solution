class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = 0
        second = 0
        ans = []
        while second < len(secondList) and first < len(firstList):
            x1 = firstList[first][0]
            x2 = secondList[second][0]
            y1 = firstList[first][1]
            y2 = secondList[second][1]
            if x1 < x2:
                if x2 <= y1:
                    if y1 < y2:
                        ans.append([x2, y1])
                        first += 1
                    else:
                        ans.append([x2, y2])
                        second += 1
                else:
                    first += 1                
            elif x1 >= x2:
                if x1 <= y2:
                    if y1 > y2:
                        ans.append([x1,y2])
                        second += 1
                    else:
                        ans.append([x1,y1])
                        first += 1
                else:
                    second += 1
        return ans


        