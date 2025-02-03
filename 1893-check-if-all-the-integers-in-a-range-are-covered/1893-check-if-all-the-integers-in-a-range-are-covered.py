class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # left 2, right = 5----> 2,3,4,5
        container = set()
        for r in ranges:
            a, b  = r
            for i in range(a,b+1):
                container.add(i)
        for i in range(left, right+1):
            if i not in container:
                return False
        return True

        