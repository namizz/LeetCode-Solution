class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split('.')
        arr2 = version2.split('.')
        print(arr1, arr2)
        n = max(len(arr1), len(arr2))
        for i in range(n):
            x, y = 0, 0
            if i < len(arr1):
                x = int(arr1[i])
            if i < len(arr2):
                y = int(arr2[i])
            if x > y:
                return 1
            elif x < y:
                return -1
        return 0


        