class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        #intervals of [starti, endi]
        #starti is unique
        #find right interval , right interval is startj >= endi for i interval the right interval is j, startj is minimized
        #compare endi with all startj
        #1,2,3
        def searcher(l,r,arr,e):
            while l <= r:
                mid = (l +r)//2
                if arr[mid] == e:
                    return mid
                elif arr[mid] > e:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        hashmap = {}
        arr = []
        ans = [-1]*len(intervals)
        for i in range(len(intervals)):
            s,e = intervals[i]
            hashmap[s] = i
            arr.append(s)
        arr.sort()
        for i in range(len(intervals)):
            s, e = intervals[i]
            l = 0
            r = len(arr) - 1
            if arr[l] <= e and e <= arr[r]:
                index = searcher(l,r,arr,e)
                ans[i] = hashmap[arr[index]]
        return ans
            



        