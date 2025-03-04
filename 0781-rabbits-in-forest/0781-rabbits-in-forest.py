class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # interview rabbit "how many rabbit have the same color"
        # ans = []
        # return minimum of number of rabbits
        # ----------------------------------------
        # count the same answer
        # 1: think of 2
        # if there 2 1's they know each other there are 2 rabbits
        # if there 1 1's there are 2 rabbits
        hashmap = Counter(answers)
        ans = 0
        # 3,3,3,3,3,3,3,3,3--> 3:10---> 10//4=2, 10%4=2
        for k in hashmap:
            q = hashmap[k] // (k+1)
            r =  hashmap[k] % (k+1)
            ans += q*(k+1)
            if r:
                ans += (k+1)
                
        return ans



        