class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        #given nums=[] l,r
        # return minimum sum of sub of array > 0
        # sub-array length can be l upto r
        # method1: iterate in l and l +1 and ...r then find the sum by using sliding window
        # method2: create an array of length r-l+1, then compute the sum in sliding window and check for
        # minimum with their range and print the smallest
        # loop--> len()-l, window size is l+1, no num is saved in arr <= 0
        total = sum(nums[:l-1])
        print('total', total)
        mini = float(inf)
        for i in range(l-1, len(nums)):
            total += nums[i]
            print('added', nums[i], 'total', total)
            temp = total
            for j in range(r-l+1):
                if temp > 0:
                    mini = min(mini, temp)
                if i + j + 1 < len(nums):
                    temp += nums[i + j + 1]  
                else:
                    break
            total -= nums[i-(l-1)]
            print('deleted', nums[i-(l-1)])
        return mini if mini != float(inf) else -1


                


