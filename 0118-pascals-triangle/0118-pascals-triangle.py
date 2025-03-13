class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 2-> 0, ans[0]+ans[1], ans[1]+ans[2], 0
        # 3->0, ans[1]+ans[2], ans[2]+ ans[1], 0
        # 4->0, ans[1]+ans[2], ans[2]+ans[3], ans[3]+ans[4],0
        arr = [0,1,0]
        ans = []
        for i in range(numRows):
            ans.append(arr[1:-1])
            temp = []
            temp.append(0)
            for i in range(len(arr)-1):
                temp.append(arr[i]+arr[i+1])
            temp.append(0)
            arr = temp
        return ans


        