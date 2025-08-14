class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0]*1002
        for num, st, end in trips:
            arr[st] += num
            arr[end] -= num
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
        # print(arr)
        return max(arr) <= capacity




        