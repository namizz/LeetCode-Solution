1class Solution:
2    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
3        # arithmetic    -> len(arr) >= 3, 
4        #               -> consecutive elements have same difference with other consecutive on sub array (arr)
5        # 
6        n = len(nums)
7        if n < 3:
8            return 0
9
10        ans = 0
11        l = 0
12        for r in range(2,len(nums)):
13            if nums[r] - nums[r - 1] != nums[r - 1] - nums[r - 2]:
14                k = r - l
15
16                if k >= 3:
17                    ans += (k - 1) * (k - 2) // 2
18                l = r - 1
19
20
21        k = n - l
22        if k >= 3:
23            ans += (k - 1) * (k - 2) // 2
24        return ans
25            
26
27
28            
29
30
31        
32        