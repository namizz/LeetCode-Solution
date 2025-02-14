class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # take 2 element from the sort array and then do the operation
        # replace it and remove one element 
        # 
        nums.sort(reverse = True)
        n = len(nums)
        # print(nums)
        result = min(nums[-1], nums[-2])*2 + max(nums[-1], nums[-2])
        while result < k:
            x = nums.pop()
            y = nums.pop()
            result = min(x,y)*2 + max(x,y)
            nums.append(result)
        # print(nums)
        return n - len(nums) 


        