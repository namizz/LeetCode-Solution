class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            p1, p2 = 0,0
            ans = []
            while p1 < len(left) and p2 < len(right):
                if left[p1] < right[p2]:
                    ans.append(left[p1])
                    p1 += 1
                else:
                    ans.append(right[p2])
                    p2 += 1
            ans.extend(left[p1:])
            ans.extend(right[p2:])
            return ans           
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left_a = self.sortArray(nums[:mid])
        right_a = self.sortArray(nums[mid:])

        return merge(left_a, right_a)

        