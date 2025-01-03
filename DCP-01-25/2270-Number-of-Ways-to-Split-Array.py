class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # num=[]
        # split at i if i+1 >= n-(i+1) and one element after i
        # return the num of split
        # prefix_sum
        #front_ps
        #back_ps
        #iterate front_ps and compare with back_ps if back_ps is greater or equal add numOfsplit
        front_ps = []
        total = 0
        ans = 0
        for i in nums:
            total += i
            front_ps.append(total)
        for i in range(len(front_ps)-1):
            if front_ps[i] >= (total-front_ps[i]):
                ans += 1
        return ans

        