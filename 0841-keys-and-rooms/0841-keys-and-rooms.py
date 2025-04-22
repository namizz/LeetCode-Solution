class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        hashmap = {}
        for i in range(len(rooms)):
            hashmap[i]= rooms[i]
        # print(hashmap)
        visited = set([0])
        queue = deque(hashmap[0])
        while queue:
            for i in range(len(queue)):
                x = queue.popleft()
                if x not in visited:
                    visited.add(x)
                    queue.extend(hashmap[x])
        # print(visited)
        return len(visited) == len(rooms)
        