class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hash = {}
        for i in range(len(names)):
            hash[heights[i]] = names[i]
        sort_h = sorted(heights)
        ans = []
        print(sort_h, heights)
        for i in range(len(sort_h)-1, -1, -1):
            ans.append(hash[sort_h[i]])
        return ans


        # for i in range(len(names)):
        #     for j in range(i+1,len(names)-1):
        #         if heights[j] < heights[j+1]:
        #             heights[j],heights[j+1]= heights[j+1], heights[j]
        #             names[j],names[j+1] = names[j+1],names[j]
        # return names
                
        