class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            _min = i
            for j in range(i+1,len(names)):
                if heights[_min] < heights[j]:
                    _min = j
            if i != _min:
                heights[_min], heights[i] = heights[i], heights[_min]
                names[_min], names[i] = names[i], names[_min]
        
        return names