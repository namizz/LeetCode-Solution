class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        arr = [0]*(max(costs)+1)
        for i in costs:
            arr[i] += 1
        ans = 0
        for i in range(len(arr)):
            while arr[i] > 0:
                if coins >= i:
                    ans += 1
                    arr[i] -= 1
                    coins -= i
                else:
                    return ans
        return ans


        
        