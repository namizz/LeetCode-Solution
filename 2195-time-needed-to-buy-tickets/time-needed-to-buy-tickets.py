class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # time required for person k to buy a ticket(1sec for 1ticket)
        #if the k > i
        # compare ticket[k] with i
        # add ticket[k]/ticket[k]-1 if ticket[i] is  grater
        # else add ticket[i]
        #5,2,4,1
        #for k = 4 ans = 4
        #for k = 3 ans = 
        ans = 0
        for i in range(len(tickets)):
            if tickets[i] >= tickets[k]:
                ans += tickets[k]
                if k < i:
                    ans -= 1
            else:
                ans += tickets[i]
        return ans



        