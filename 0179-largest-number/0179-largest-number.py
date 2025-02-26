class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = []
        arr = []
        for i in range(len(nums)):
            leng = len(str(nums[i]))-1
            first = nums[i]// 10**leng
            arr.append((first, nums[i]))

        sorted_arr = sorted(arr, key=lambda x: str(x[1])*10 , reverse=True)
        for _,i in sorted_arr:
            ans.append(str(i))
        return "".join(ans) if ans[0] != "0" else "0"


        