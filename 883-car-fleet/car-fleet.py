class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = {}
        for i in range(len(position)):
            ps[position[i]] = speed[i]
        pos = sorted(position)
        pos.reverse()
        stack = []
        for i in range(len(pos)):
            dl = target - pos[i]
            t = dl/ps[pos[i]]
            if stack and stack[-1] >= t:
                t = stack.pop()
            stack.append(t)
        return len(stack)




        # n- car
        # 0 - target mile
        # postion(mile) and speed(mile/hr) of n cars are given
        # car cannot pass another car
        # car fleet at destination
        # solution
        #what matter here is time
        # 1hr,1hr,12hr,7hr,3hr
        # decreasing monotonic stack---->car fleet--stack[-1]---time should be in decreasing order
        # store on stack their time
        # if less: comprare if the it stick to the previous car: else: stack.append(time)
        # if greater: compare if it stick to the upcoming car: stack.pop() stack.append()
        #example target = 13
        #[10,8, 1,    5, 3, 0]
        #[ 2,2, 3(9?),8, 4, 2]
        #[ 2,4, 4,1, 3,12]///////////////////////////speeddddddddd
        #[ 3,5,12,8,10,13]distance left
        # time = []

        # stack = []
        # count = 0
        # for i in range(len(position)):
        #     if stack:
        #         if time[stack[-1]] > time[i] and position[stack[-1]] < position[i]:
        #             stack.pop()
        #             count -= 1 
        #         while stack and position[i] > position[stack[-1]] and time[i] > time[stack[-1]]:
        #             stack.pop()
        #             count -= 1             
        #     stack.append(i)
        #     count += 1

        # return count

        #if p[1] > p[2] and t[1] > t[2]
        #if p[1] > p[2] and t[2] < t[1]
        
        
        #:loop : postion 2: time and counter-=1///////////
        #if p[2] > p[1] and t[2] < t[1]: stack.append??????????????
        #if p[2] < p[1] and t[1] > t[2]: none

            

        

        