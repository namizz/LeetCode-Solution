class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        #prefix sum of the shift from right to left
        #update the value of s in term of the prefix sum of shift
        for i in range(len(shifts)-2,-1,-1):
            shifts[i] += shifts[i+1]
        print(shifts)
        ans = []
        for i in range(len(s)):
            letter = ord(s[i])-97
            shifted = chr((shifts[i]+letter)%26 + 97)
            ans.append(shifted)
        print(ans)
        return "".join(ans)
