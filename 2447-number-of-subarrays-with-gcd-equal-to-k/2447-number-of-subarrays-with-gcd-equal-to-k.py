class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        for i in range(len(nums)):
            g = 0
            for j in range(i,len(nums)):
                g = gcd(g,nums[j])
                if g == k:
                    ans += 1
                elif g < k:
                    break
        return ans

                    


        