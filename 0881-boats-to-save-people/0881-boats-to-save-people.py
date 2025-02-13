class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        contain = set()
        ans = 0
        for i in range(len(people)-1,-1,-1):
            temp = 0
            if i not in contain:
                temp += people[i]
                ans += 1
                contain.add(i)
                for j in range(i-1, -1,-1):
                    # print(temp+people[j], limit, contain)
                    if temp + people[j] <= limit and j not in contain:
                        contain.add(j)
                        temp += people[j]
                        break
                        
            # print("contain", contain)
            # print("people", people[:i+1])

        return ans
                
            
                    
        


        
        