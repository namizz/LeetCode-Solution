class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        leng = len(code)
        for i in range(len(code)):
            temp = 0
            j = 0
            if k > 0:
                while j < k:
                    temp += code[(i+1+j)%leng]
                    j += 1
            elif k < 0:
                while j < abs(k):
                    temp += code[(i-1-j)% leng]

                    j += 1
            ans.append(temp)  
            i += 1
        return ans

        