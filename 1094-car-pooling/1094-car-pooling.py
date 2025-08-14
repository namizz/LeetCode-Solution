class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        trips.sort(key=lambda x:x[1])
        people = 0
        for num,st,end in trips:
            if heap and heap[0][0] <= st:
                print(heap)
                e,n = heapq.heappop(heap)
                people -= e
            if num + people > capacity:
                return False
            heapq.heappush(heap, [end, num])
            people += num
            # print(heap)
        return True
            



        