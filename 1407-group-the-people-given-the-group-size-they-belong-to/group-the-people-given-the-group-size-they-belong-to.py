class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        hashmap = {}
        for i in range(len(groupSizes)):
            value = groupSizes[i]
            if value in hashmap:
                hashmap[value].append(i)
                if len(hashmap[value]) == value:
                    ans.append(hashmap[value])
                    hashmap.pop(value)
            else:
                hashmap[value] = [i]
                if len(hashmap[value]) == value:
                    ans.append(hashmap[value])
                    hashmap.pop(value)
 
        
        for i in hashmap.values():
            ans.append(i)
        return ans
        