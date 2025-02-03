class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split(" ")
        ans = []
        max_l = 0
        for i in range(len(arr)):
            max_l = max(len(arr[i]), max_l)
        i = 0
        while i < max_l:
            temp = []
            for j in range(len(arr)):
                if i < len(arr[j]):
                    if len(temp) < j:
                        temp.extend([" "]*(j-len(temp)))
                    temp.append(arr[j][i])                    
            ans.append("".join(temp))
            i += 1
        return ans
                



            
        