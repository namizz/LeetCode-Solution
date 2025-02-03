class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hashmap = {}
        for game in matches:
            w, l = game
            if w not in hashmap:
                hashmap[w] = 0
            if l not in hashmap:
                hashmap[l] = 1
            elif l in hashmap:
                hashmap[l] += 1
        zeros = []
        ones = []
        for i in hashmap:
            if hashmap[i] == 0:
                zeros.append(i)
            elif hashmap[i] == 1:
                ones.append(i)
        return [sorted(zeros), sorted(ones)]

        