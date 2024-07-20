class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        j = 0
        if len(arr) < 2:
            return False
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                j += 1
            
            elif arr[i] == arr[i+1] or arr[0] > arr[1]:
                return False
            else:
                break
        if j == len(arr)-1:
            return False
        for i in range(j,len(arr)-1):
            if arr[i] > arr[i+1]:
                j+=1
            else:
                return False
        if j == len(arr) - 1:
            return True
        return False
            
        