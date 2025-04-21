class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # 1, -2, 2
        # added from min
        # upto from max
        for i in range(1,len(differences)):
            differences[i] += differences[i-1]
        print(differences)
        differences.append(0)
        start = lower - min(differences) 
        upto = upper - max(differences)
        # 6 10 3 5
        # +6 +53 = 60
        return max(0, upto-start+1)