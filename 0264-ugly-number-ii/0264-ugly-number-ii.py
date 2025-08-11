class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        contain = set([1])
        for i in range(1,n):
            k = heapq.heappop(heap)
            if k*2 not in contain:
                heapq.heappush(heap, k*2)
                contain.add(k*2)
            if k*3 not in contain:
                heapq.heappush(heap, k*3)
                contain.add(k*3)
            if k*5 not in contain:
                heapq.heappush(heap, k*5)
                contain.add(k*5)
        return heapq.heappop(heap)





        

        