class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lp = 0
        rp = len(citations) - 1
        length = len(citations)
        while lp <= rp:
            mid = (lp+rp)//2
            if(length - mid) == citations[mid]:
                return length - mid
            elif (length - mid) < citations[mid]:
                rp = mid - 1
            else: 
                lp = mid + 1
        if citations[length - 1] <= 0:
            return 0
        return length-lp

        