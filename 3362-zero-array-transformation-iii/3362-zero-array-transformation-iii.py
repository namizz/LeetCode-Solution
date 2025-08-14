class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        heap = []
        arr = [0]*(len(nums)+1)
        j = 0
        used = 0
        for i in range(len(nums)):
            used += arr[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            while used < nums[i] and heap and -heap[0] >= i:
                used += 1
                arr[-heappop(heap)+1] -= 1
            if used < nums[i]:
                return -1
        return len(heap)

        
        
        