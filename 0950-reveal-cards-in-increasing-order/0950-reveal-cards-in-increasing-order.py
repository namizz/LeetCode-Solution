class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # rearrange it in increasing order
        # card are faced down
        # you take i card reveal and i+1 to the bottom of the cards(repeat)
        # reveal the card in ascending order
        # sort them
        # [2,13,3,11,5,17,7]
        deck.sort()
        queue = deque([i for i in range(len(deck))])
        ans = [0]* len(deck)
        for i in range(len(deck)):
            index = queue.popleft()
            ans[index] = deck[i]
            if queue:
                queue.append(queue.popleft())
        return ans
            
        