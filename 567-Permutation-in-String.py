class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # window size should static which is equal to the length of s1
        # create a window and save it on dictonary and 
        # if the s1 in exactly in dictonary return true other wise update window
        # s1 should be used in dictonary form
        sub = Counter(s1)
        hashmap = Counter(s2[:len(s1)])
        for i in range(len(s2)-len(s1)):#check for edge case
            edge = 0
            for j in sub:
                edge += 1
                if j not in hashmap or sub[j] != hashmap[j]:
                    break
                if edge == len(sub):
                    return True
            if s2[i+len(s1)] not in hashmap:
                hashmap[s2[i+len(s1)]] = 0
            hashmap[s2[i+len(s1)]] += 1
            hashmap[s2[i]] -= 1
        edge = 0
        for j in sub:
            edge += 1
            if j not in hashmap or sub[j] != hashmap[j]:
                break
            if edge == len(sub):
                return True
        return False

            
            

                    
        