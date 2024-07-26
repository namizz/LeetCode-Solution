
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) -1
        j=0
        while(left < right):
            s[right],s[left]= s[left],s[right]
            left+=1
            right-=1
        print(s)
            

