class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        hashmap = defaultdict(list)
        for a,b,price in flights:
            hashmap[a].append((b, price))
            if b not in  hashmap:
                hashmap[b] = []
        path = [float(inf)]*(n+1)
        path[src] = 0
        queue = deque([(src,0, 0)])
        print(hashmap)
        while queue:
            x,cst, stp = queue.popleft()
            if stp > k:
                continue
            for neg, price in hashmap[x]:
                if price + cst >= path[neg]:
                    continue
                path[neg] = price + cst
                queue.append((neg, path[neg], stp+1))
            print(path)
        print(path)
        return path[dst] if path[dst] != float(inf) else -1
        

        