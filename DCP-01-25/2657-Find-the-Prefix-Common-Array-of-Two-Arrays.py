class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # A=[], B=[]
        # return C=[] where 
        # C[i] = number present before or at A[i] and B[i]
        # { 1:0, 3:1, 2:2, 4:3}
        # hashamp[3] >= 0:
        # hashmap[1] >= 1 , 1
        # hashmap[2] >=2 , 2
        # hashmap[4], 3
        #[0,2,3,4]
        hashmap = {}
        for i in range(len(A)):
            hashmap[A[i]] = i
        count = 0
        ans = [0]*(len(A))
        for i in range(len(B)):
            if hashmap[B[i]] <= i:
                count += 1
            else:
                ans[hashmap[B[i]]] += 1
            ans[i] += count
            count = ans[i]
        return ans

        