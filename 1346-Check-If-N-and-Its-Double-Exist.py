class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = Counter(arr)
        for num in arr:
            if num /2 in hashmap:
                if num == 0 and hashmap[num] > 1:
                    return True
            elif num*2 in hashmap:
                return True
        return False
                
        