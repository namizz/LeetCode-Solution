class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        max_weight = sum(weights)
        min_weight = max(weights)
        # 1,2,3,4,5,6,7,8,9,10
        # 10, 55

        def num_days(weight):
            days = 1
            carry = 0
            for i in weights:
                if carry + i <= weight:
                    carry += i
                else:
                    days += 1
                    carry = i
            return days 
            
        # 32
            
            
        l = min_weight
        r = max_weight
        ans = 0
        while l <= r:
            mid = (l+r)//2
            temp = num_days(mid)
            if temp > days:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1
        return ans
        
                


        # number of days(weight):
        # iterate through the numbers till he collect the maximum weight on the specific day and mark the weights the is heald
        # the weight should be minum as much as possible
        