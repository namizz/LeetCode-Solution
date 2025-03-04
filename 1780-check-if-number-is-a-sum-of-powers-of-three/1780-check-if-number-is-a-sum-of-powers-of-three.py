class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # n:int 
        # return True/False
        # if n-> 3^a+3^b+... if a!= b True else false
        # n%3=1---> we could make by using x + 3^0
        # n//3 should be an integer where n%3 <= 1
        # 12-> 4*3 + 1-> 4//3 = 1 --> 3* (3*1 + 1) + 1 --> 3*3 + 3 + 1
        # 91 -- 91//3, 91%3 --> 30 * 3 + 1-- 30//3---> 3*(10*3 + 0)+ 1---> 10//3--->3*(3*(3*3+1)+0)+1--> 
        # 3*3*3*3 + 3*3*3 + 1
        # from the above just constantly divide the quotient with 3
        # 1, 9, 81
        # arr = []
        # this contains remainder, quotient, quotient is replace(multiply 3) if no remainder else quotient append
        # 92
        # 3*3+1
        # 2, 9, 81
        # 7
        # 7//3= 2
        # 1, 6
        # check if the array are multiple of 3
        # sqrt(num) == an integer

        while n > 0:
            r = n%3
            if r == 2:
                return False
            n //= 3
        
        return True
            

         
        
        