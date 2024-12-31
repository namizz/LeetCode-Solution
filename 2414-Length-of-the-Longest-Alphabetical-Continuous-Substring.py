class Solution:
    def canChange(self, start: str, target: str) -> bool:
        #L can move to left if the space is occupied by blank
        #R can move to right if it is occupied by blank
        #if start string can give target by any of move return True
        #
        #condition we can't get the target
        #if the string s and target is different
        #on comparing the location of target and s of any L if the target[pos] > start[pos] 
        #on comparing the location of target and s of any R if the start[pos] > target[pos]
        #how to compare t=[], s=[]
        #if the string are similar iterate
        #if we get L in target and blank in start L+=1(indicate how many left we should get in start)
        #if we get L in start and L<=0 return false
        #if we get R in start and blank in target R += 1(indicate how many right we should get in target)
        #if we get R in target and R<=0 return false
        L ,R = 0, 0
        for i in range(len(start)):
            if start[i] == target[i]:
                if (start[i] =='L' and R > 0) or(target == 'R' and L > 0):
                    return False
                continue
            elif target[i] =='L' and start[i]=='_' and R == 0:
                L += 1
            elif start[i]=='R' and target[i]=='_' and L == 0:
                R += 1
            elif start[i] =='L' and target[i]=='_':
                if L <= 0:
                    return False
                L -= 1
            elif target[i] =='R' and start[i]=='_':
                if R <= 0:
                    return False
                R -= 1
            else:
                return False
        return True if L==R==0 else False




        