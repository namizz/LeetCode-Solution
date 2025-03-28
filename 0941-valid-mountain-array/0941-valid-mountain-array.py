class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        j = 0
        increase = False
        decrease = False
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                j += 1
                increase = True
            elif arr[i] == arr[i+1] or arr[0] > arr[1]:
                return False
            else:
                break
        for i in range(j,len(arr)-1):
            if arr[i] > arr[i+1]:
                j+=1
                decrease = True
            else:
                return False
        return increase and decrease
            
        