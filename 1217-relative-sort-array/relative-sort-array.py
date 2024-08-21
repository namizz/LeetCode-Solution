class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_arr1 = Counter(arr1)
        ans = []
        for num in arr2:
            ans.extend([num] * hash_arr1[num])
            del hash_arr1[num]
        remain = sorted(hash_arr1.elements())
        ans.extend(remain)
        return ans
        

        