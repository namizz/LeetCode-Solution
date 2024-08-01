class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        i = 0 
        temp = left
        while i < len(ranges):
            if ranges[i][0] <= temp and ranges[i][1] >= temp:
                if ranges[i][1] >= right:
                    return True
                else:
                    temp = ranges[i][1] + 1
                    i = -1
            i += 1
        return False

            
            
        # interval = None
        # for i in range(len(ranges)):
        #     if ranges[i][0] <= left and ranges[i][1] >= left:
        #         interval = i
        #         break
        # if interval is None:
        #     return False
        # else:
        #     for i in range(interval,len(ranges)):
        #         if ranges[i][1]>= right:
        #             return True
        #         elif i < len(ranges)-1 and ranges[i][1]+1 <= ranges[i+1][0]:
        #             continue
        #         else:
        #             return False

        