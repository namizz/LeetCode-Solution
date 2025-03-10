class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for ops in logs:
            if ops == "../":
                if count:
                    count -= 1
            elif ops != "./":
                count += 1
        return count 
        