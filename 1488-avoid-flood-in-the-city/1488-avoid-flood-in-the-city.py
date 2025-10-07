class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # rains = [] on which lake does the rain rains.
        # to avoid flood we dry the lakes that may cause flood. 
        # we continue iterating through rains until rains[i] == 0:
        # if there is flood before any 0's return []
        # continue the iterating count the number of 0's you get
        # when ever their is probablity of flooding use 0's day to dry the full lake
        # we need to know the postions of full lakes and zeros position
        zero = []
        pt = 0
        ans = [-1]*len(rains)
        hashmap = {}
        for i in range(len(rains)):
            print(hashmap)
            print(zero)
            if not rains[i]:
                zero.append(i)
            else:
                if rains[i] in hashmap:
                    j = bisect_right(zero, hashmap[rains[i]])
                    if j == len(zero):
                        return []
                    ans[zero[j]] = rains[i]
                    zero.pop(j)
                hashmap[rains[i]] = i
            
        for i in zero:
            ans[i] = 1
        return ans
            
            
            
            
        