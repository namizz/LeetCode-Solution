class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        hashmap = {'W':0,'B':0}
        for i in range(k):
            hashmap[blocks[i]] += 1
        _min = hashmap['W']
        for i in range(k, len(blocks)):
            hashmap[blocks[i]] += 1
            hashmap[blocks[i-k]] -= 1
            _min = min(_min, hashmap['W'])
        return _min
        