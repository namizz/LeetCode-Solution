class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        j = -1
        for i in range(len(arr)-1, -1,-1):
            if arr[i] > j:
                arr[i],j = j, arr[i]
            else:
                arr[i] = j
        return arr

       


       

        
        