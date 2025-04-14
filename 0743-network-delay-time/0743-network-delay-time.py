class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hashmap = defaultdict(list)
        for a,b,t in times:
            hashmap[a].append((b,t))
            if b not in hashmap:
                hashmap[b] = []
        # print(hashmap)            
        ans = 0
        queue = deque([k])
        arr = [float(inf)]*(n+1)
        arr[k] = 0
        while queue:
            for neg in hashmap[queue[0]]:
                # operate short path
                node, t = neg
                if t+arr[queue[0]] >= arr[node]:
                    continue
                arr[node] = t + arr[queue[0]]
                queue.append(node)
            queue.popleft()
            # print(arr)
        ans = max(arr[1:]) 
        return ans if ans != float(inf) else -1
        



        return -1
        