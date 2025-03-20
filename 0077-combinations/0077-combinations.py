class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans,path = [], []
        def backtrack(i,combination):
            if i > n:
                if len(combination) == k:
                    ans.append(combination[:])
                return
            combination.append(i)
            backtrack(i+1,combination)
            combination.pop()
            backtrack(i+1,combination)

        backtrack(1,[])
        return ans

        