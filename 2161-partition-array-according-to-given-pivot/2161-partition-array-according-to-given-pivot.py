class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a, b, c = [], [], []
        for i in range(len(nums)):
            if nums[i] > pivot:
                b.append(nums[i])
            elif nums[i] < pivot:
                a.append(nums[i])
            else:
                c.append(nums[i])
                
        return a+c+b