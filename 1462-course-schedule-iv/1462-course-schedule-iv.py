class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # numCourse: int, prerequisites= [[]], queries = [[]]
        # true if queries[j] =[ui, vi] where ui is prerequsite for vi
        # check if quries are true or false
        # make a storage which could be easily accessed by the querie where when you inter vi it check if ui is one of the prerequiste or no
        # make a 2d array based on the course number and make 1 if the course is dependent
        # else make 0
        # this is called adjecent matrix
        # [1,0,1]
        # [0,0,0]
        # [0,1,0]
        # 
        arr = [[0]*numCourses for i in range(numCourses)]
        for c,r in prerequisites:
            arr[r][c] = 1
        print(arr)
        queue = deque()
        ans = []
        for i in range(numCourses):
            for j in range(numCourses):
                for k in range(numCourses):
                    if arr[i][k] and arr[k][i]:
                        arr[i][j] == 1
        for ui, vi in queries:
            ans.append(arr[vi][ui] == 1)  
        return ans