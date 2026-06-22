1class Solution:
2    def totalFruit(self, fruits: List[int]) -> int:
3        # left pointer ---> if the hashmap value is morethan too, until it became two.
4        # right pointer ---> move to right if the hashmap length is not morethan 2
5        hashmap = {}
6        l = 0
7        ans = 0
8        for r in range(len(fruits)):
9            f = fruits[r]
10            hashmap[f] = hashmap.get(f,0) + 1
11        # [0,1,2,2]
12
13            if len(hashmap) > 2:
14                ans = max(ans, r-l)
15            while len(hashmap) > 2:
16                lf = fruits[l]
17                hashmap[lf] -= 1
18                if not hashmap[lf]:
19                    del hashmap[lf]
20                
21                l += 1
22
23        return max(ans, len(fruits)-l)
24        