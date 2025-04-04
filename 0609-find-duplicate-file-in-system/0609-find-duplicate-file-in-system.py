class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = {}
        ans = []
        for p in paths:
            root, *rest = p.split()
            for i in rest:
                name, content = i.split('.txt')
                if content not in hashmap:
                    hashmap[content] = [(root, name)]
                else:
                    hashmap[content].append((root, name))
        for k in hashmap:
            temp = []
            for value in hashmap[k]:
                temp.append(value[0]+"/"+value[1]+".txt")
            if len(temp) > 1:
                ans.append(temp)
        return ans
            
            
            

        