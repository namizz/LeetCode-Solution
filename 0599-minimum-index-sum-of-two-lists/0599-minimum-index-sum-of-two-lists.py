class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = {}
        for i in range(len(list1)):
            hashmap[list1[i]] = i
        _min = float(inf)
        ans = []
        for i in range(len(list2)):
            
            if list2[i] in hashmap:
                diff = abs(hashmap[list2[i]]+i)
                if _min > diff:
                    _min = diff
                    ans = [list2[i]]
                elif _min == diff:
                    ans.append(list2[i])
        return ans

                


        

        