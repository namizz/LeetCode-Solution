class Solution:  
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # arr = [0]*n 
        # shifts-->start, end, dir------------>iterate
        # arr[start:end+1]---> 1 or -1
        # iterate s if arr
        arr = [0]*(len(s)+1)
        for start, end, direction in shifts:
            if direction == 1:
                arr[start] += 1
                if end + 1 < len(s): 
                    arr[end+1] -= 1
            else:
                arr[start] -= 1
                if end + 1< len(s):
                    arr[end + 1] += 1
        
        for i in range(1,len(s)):
            arr[i] += arr[i-1]
        ans = []
        for i in range(len(s)):
            asc = ord(s[i]) - 97
            letter = (arr[i]+asc)%26 
            ans.append(chr(letter + 97)) 
        return "".join(ans)
        

        