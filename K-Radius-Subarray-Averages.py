1class Solution:
2    def getAverages(self, nums: List[int], k: int) -> List[int]:
3        # nums = []
4        # k = int
5        # sub_arr = (i-k, i+k)
6        # i < k or i > len(arr) - k ---> k-av = -1
7        # avgs = [] , len(n)
8        # avgs[i] = k-av for subarray center at index i
9        # solution
10        # nums = [7,4,3,9,1,8,5,2,6] k = 3
11        # if i < k and i > len(arr) - k, k-av = -1
12        # avgs = [-1,-1,-1, -,-,- ,-1,-1,-1]
13        # total = 
14        total = 0
15        avgs = [-1] * len(nums)
16        window = 2*k+1
17        if window > len(nums):
18            return avgs
19
20        for i in range(window):
21            total += nums[i]
22
23        for i in range(window, len(nums)):
24            indx = i-window
25            avgs[indx+k] = total // window
26            total += nums[i]
27            total -= nums[i-window]
28        avgs[len(nums)-window+k] = total//window
29        return avgs
30
31
32        
33        
34        