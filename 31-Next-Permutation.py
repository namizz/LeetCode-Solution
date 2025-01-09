class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        # arr = []
        # return arr
        # swap arr elements
        # iterate throught arr, find where arr[i-1] < arr[i]
        # find the greater than arr[i-1] and less than comparble in the right of the arr[]
        # when you find swap the arr[i-1] and arr[i]
        # after swap sort the rest array
        left = -1
        right = -1
        for i in range(len(nums)-2, -1,-1):
            if nums[i] < nums[i+1]:
                left = i
                break
        if left == -1:
            nums.reverse()
            return
        for i in range(len(nums)-1,-1,-1):
            if nums[left] < nums[i]:
                right = i
                break
        nums[left], nums[right] = nums[right], nums[left]
        nums[left + 1:] = reversed(nums[left + 1:])
            
        