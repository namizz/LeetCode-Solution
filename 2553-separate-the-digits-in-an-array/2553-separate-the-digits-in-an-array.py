class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            temp = []
            while i > 0:
                temp.append(i%10)
                i //= 10
            ans.append(i) if not temp else ans.extend(temp[::-1])
        return ans
        