class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0]*(len(s)+1)
        for i in shifts:
            l,r,di = i
            if di:
                arr[l] += 1
                arr[r+1] -= 1
            else:
                arr[l] -= 1
                arr[r+1] += 1
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
        ans = []
        for i in range(len(s)):
            letter = ord(s[i])-97
            letter += arr[i]
            letter %= 26
            letter += 97
            ans.append(chr(letter))
        return "".join(ans)
