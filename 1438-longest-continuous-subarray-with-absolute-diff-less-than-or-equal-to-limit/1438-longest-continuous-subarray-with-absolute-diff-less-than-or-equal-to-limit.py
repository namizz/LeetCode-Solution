class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # limit : int
        # sub-array= []- max-min <= limit
        # return sub-array with range <= limit
        # iterate through an array and when the condition is not satified we remove elements from the left
        # use queue
        # how do we know if the conditions is met or not
        # to get the highest number in array we need monotonic mono
        arr = deque()
        ans = 0
        mono = deque()
        decr = deque()
        # iterate through arr
        for i in range(len(nums)):
            # append elements
            arr.append(nums[i])
            # append greater elements
            while mono and mono[-1] < nums[i]:
                mono.pop()
            mono.append(nums[i])
            # append smaller elements
            while decr and decr[-1] > nums[i]:
                decr.pop()
            decr.append(nums[i])
            # if greater-current > limit eliminate until you get greater number
            while mono[0] - nums[i] > limit: 
                while arr and arr[0] != mono[0]:
                    arr.popleft()
                arr.popleft()
                mono.popleft()
            while nums[i] - decr[0] > limit: 
                while arr and arr[0] != decr[0]:
                    arr.popleft()
                arr.popleft()
                decr.popleft()
            ans = max(len(arr), ans)
        return ans
            
        