class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # minimum of sub arrays
        # their sum        
        ans = 0
        stack = []
        for r in range(len(arr)):
            while stack and stack[-1][1] > arr[r]:
                l, val = stack.pop()
                left = l - stack[-1][0] if stack else l+1
                right = r - l
                ans += (val*left*right)
            stack.append((r,arr[r]))
        for i in range(len(stack)):
            l, val = stack[i]
            left = l - stack[i - 1][0] if i > 0 else l+1
            right = len(arr) - l
            ans += (val*left*right)

        return ans % (10**9 + 7)




        