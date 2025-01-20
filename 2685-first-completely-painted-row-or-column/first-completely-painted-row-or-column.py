class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        #arr = [], mat = [[]]-----[1-m*n]
        # return i where col or row are fully painted
        #method1
        # bruteforce
        # check and iterate through the col and row if visible, every time we iterate through arr. 
        # o(n3)
        #method2 other approach
        # rows=[]
        #cols = []
        # decrease from rows and col when we iterate
        # 
        hashmap = {}
        row = len(mat)
        col = len(mat[0])
        n_r = [len(mat[0])]*len(mat)
        n_c = [len(mat)]*len(mat[0])
        for i in range(row):
            for j in range(col):
                hashmap[mat[i][j]] = [i,j]
        for i in range(len(arr)):
            a,b = hashmap[arr[i]]
            n_r[a] -= 1
            n_c[b] -= 1
            if n_r[a] == 0 or n_c[b] == 0:
                return i
        

        