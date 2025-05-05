class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # check for smaller entrys
        # then check for smaller processing time
        # ans.append(the task number)
        # add time of entry
        # add all the tasks and check for smaller processing time
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        # print(tasks)
        time = tasks[0][0]
        h = []
        i = 0
        ans = []
        while i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(h, (tasks[i][1], tasks[i][2]))
                i += 1
            # print(time, h)
            if h:
                val, idx = heapq.heappop(h)
                time += val
                ans.append(idx)
            else:
                time = tasks[i][0]

        while len(h) > 0:
            val, idx = heapq.heappop(h)
            ans.append(idx)
        return ans
        

            
            
        