class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # minimize cost of tranfer of person to A, B city
        # person we are sending to citys should be equal in number
        # we need to sort cost in terms x[0] to find min for city A
        # we need to sort in x[1] to find min for city B
        # we iterate through them if the array are different we take both
        # if the array is the same we became greedy to pick the lowest one
        arr = sorted(costs, key=lambda x:abs(x[1]-x[0]), reverse=True)
        pa = 0 
        pb = 0 
        n = len(arr)//2
        ans = 0
        for i in range(len(arr)):
            if pa < n and pb < n:
                if arr[i][0] < arr[i][1]:
                    ans += arr[i][0]
                    pa += 1
                else:
                    ans += arr[i][1]
                    pb += 1
            elif pa < n:
                ans += arr[i][0]
            elif pb < n:
                ans += arr[i][1]
        return ans
            




        