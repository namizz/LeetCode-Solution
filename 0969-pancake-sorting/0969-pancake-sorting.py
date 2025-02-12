class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(mat, k):
            return mat[::-1]+ arr[k+1:]
        i = len(arr)-1
        ans = []
        while i > 0:
            max_i = 0
            for id, num in enumerate(arr[:i+1]):
                if num > arr[max_i]:
                    max_i = id
            arr = flip(arr[:max_i+1], max_i)
            arr = flip(arr[:i+1], i)
            print(arr)
            ans.append(max_i+1)
            ans.append(i+1)
            i -= 1
        return ans


        
        