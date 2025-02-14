class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # take 2 element from the sort array and then do the operation
        # replace it and remove one element 
        # 
        nums.sort(reverse = True)
        ans = 0
        # print(nums)
        while nums[-1] < k:
            x = nums.pop()
            y = nums.pop()
            result = min(x,y)*2 + max(x,y)
            insort(nums, result, key=lambda x: -x)
            ans += 1
        # print(nums)
        return ans

        