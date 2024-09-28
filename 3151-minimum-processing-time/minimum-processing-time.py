class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        ans = 0
        for i in range(len(processorTime)):
            y = (len(tasks) - 1) - (4*i)
            ans = max(processorTime[i] + tasks[y], ans)
        return ans


        