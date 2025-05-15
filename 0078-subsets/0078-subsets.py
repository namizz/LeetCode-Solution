class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2**len(nums)):
            print(i)
            k = i
            it = 0
            temp = []
            while k > 0:
                bt = k & 1
                k >>= 1
                if bt:
                    temp.append(nums[it])
                it += 1
            print(temp)
            ans.append(temp)
        return ans

        