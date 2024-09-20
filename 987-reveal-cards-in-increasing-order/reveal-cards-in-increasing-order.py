class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        i = 0
        queue = deque([i for i in range(len(deck))])
        result = [0]*len(deck)
        while queue:
            result[queue.popleft()] = deck[i]
            i += 1
            if queue:
                queue.append(queue.popleft())
        return result



        
        
        
        