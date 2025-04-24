class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = defaultdict(int)
        hashmap = defaultdict(list)

        for crs,pre in prerequisites:
            indeg[crs] += 1
            hashmap[pre].append(crs)

        queue = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)
        # print(queue)
        # print(hashmap)
        # print(indeg)
        ans = []
        while queue:
            for i in range(len(queue)):
                x = queue.popleft()
                ans.append(x)
                for i in hashmap[x]:
                    indeg[i] -= 1
                    if not indeg[i]:
                        queue.append(i)
        # print(ans)
        return ans if len(ans) == numCourses else []

        