class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # power value
        # x -> 1
        # rules
        # x/2
        # x * 3 + 1/2
        # 
        # Given [lo, hi]
        def rec(i):
         
            if i in hashmap:
                return hashmap[i]
            if i % 2:
                k = 3*i+1
            else:
                k = i // 2
            hashmap[i] = rec(k) + 1
            return hashmap[i]


        hashmap = {1:0}
        arr = []
        for i in range(lo, hi+1):
                arr.append((i, rec(i)))
        sort_arr = sorted(arr, key=lambda x:x[1])
        print(sort_arr)
        return sort_arr[k-1][0]

            
            
            




        