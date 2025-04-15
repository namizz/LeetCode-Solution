"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hashmap = defaultdict(list)
        imp = {}
        for k in employees:
            hashmap[k.id] = k.subordinates
            imp[k.id] = k.importance
        ans = imp[id] 
        queue = deque(hashmap[id])
        while queue:
            x = queue.popleft()
            ans += imp[x]
            queue.extend(hashmap[x])
        return ans

            
        