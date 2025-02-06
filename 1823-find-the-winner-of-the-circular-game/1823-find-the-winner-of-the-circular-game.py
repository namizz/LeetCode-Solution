class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # n - people k- removed
        # return left
        friend = [i+1 for i in range(n)]
        start = 0
        while len(friend)!=1:
            pos = (start+k-1)%len(friend)
            friend.pop(pos)
            start = pos
        return friend[0]

        