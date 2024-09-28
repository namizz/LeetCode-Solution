class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        sub_arr = []
        other_arr = []
        ans = []
        k = len(arr) - 1
        n = len(arr)

        while k > 0:
            if arr[k] == n:
                k -= 1
                n -= 1
            else:
                i = k
                while i >= 0:
                    if arr[i] == n:
                        break
                    i -= 1
                sub_arr = arr[:i+1]
                # print("sub_arr", sub_arr, i+1)
                if i != 0:
                    ans.append(i+1)
                other_arr = (sub_arr[::-1] + arr[i+1:k+1])
                # print("other", other_arr, k+1)
                ans.append(k+1)
                arr = (other_arr[::-1] + arr[k+1:])
                # print(arr)
                n -= 1
                k -= 1
        return ans



        