class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        decr = deque()
        _max = float(-inf)
        ans = []
        for i in range(k):
                while decr and nums[i] > decr[-1]:
                    decr.pop()
                decr.append(nums[i])
        if decr:
            ans.append(decr[0])
        for i in range(k, len(nums)):
            while decr and nums[i] > decr[-1]:
                decr.pop()
            decr.append(nums[i])
            ans.append(decr[0])
            if decr and decr[0] == nums[i-k]:
                decr.popleft()
            
        return ans
            


        