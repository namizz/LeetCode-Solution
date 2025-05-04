class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        x = heapq.heappop(nums)
        y = heapq.heappop(nums)
        ans = 0
        while x < k:
            ans += 1
            heapq.heappush(nums, min(x,y)*2 + max(x,y))
            if len(nums) >= 2:
                x = heapq.heappop(nums)
                y = heapq.heappop(nums)
            else:
                break

        return ans

        