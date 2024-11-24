class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # make dic1 that contain the words and their index
        # common contain the word in dict1 and list2 and their sum index
        # iterate throught the common and find the least index sum and store it on ans=[]
        dic1 = {}
        common = {}
        ans = []
        #hashmap of word and indexx of list 1
        for i in range(len(list1)):
            dic1[list1[i]] = i
        #common words with their sum index
        for i in range(len(list2)):
            if list2[i] in dic1:
                common[list2[i]] = dic1[list2[i]] + i

        least = len(list1) + len(list2) 
        for i in common:       
            if common[i] < least:
                ans = [i]
                least = common[i]
            elif common[i] == least:
                ans.append(i)
        return ans
            

        