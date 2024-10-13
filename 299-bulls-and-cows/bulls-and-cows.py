class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hashmap = Counter(secret)
        b = 0
        c = 0
        set1 = set()
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                set1.add(i)
                b += 1
                if hashmap[guess[i]] == 1:
                    hashmap.pop(guess[i])
                else:
                    hashmap[guess[i]] -= 1
        for i in range(len(guess)):
            if guess[i] in hashmap and i not in set1:
                c += 1
                if hashmap[guess[i]] == 1:
                    hashmap.pop(guess[i])
                else:
                    hashmap[guess[i]] -= 1

        return ""+str(b)+"A"+str(c)+"B"

        