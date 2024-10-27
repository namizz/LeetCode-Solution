class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        neg_arr = []
        pos_arr = []
        turn = True
        for i in range(len(nums)):
            if nums[i] > 0:
                pos_arr.append(nums[i])
            else:
                neg_arr.append(nums[i])
        j = 0
        turn = True
        while j < len(pos_arr):
            ans.append(pos_arr[j])
            ans.append(neg_arr[j])
            j += 1
        return ans

        