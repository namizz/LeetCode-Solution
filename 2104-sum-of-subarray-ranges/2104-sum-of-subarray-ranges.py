class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        dec = []
        inc = []
        _max = 0
        _min = 0
        for r in range(len(nums)):
            while dec and dec[-1][1] < nums[r]:
                l, val = dec.pop()
                left = l - dec[-1][0] if dec else l+1
                right = r-l
                _max += (val*right*left)
            dec.append((r,nums[r])) 
            

            # print("dec", dec)
            # print(_max)
            while inc and inc[-1][1] > nums[r]:
                l, val = inc.pop()
                left = l - inc[-1][0] if inc else l+1
                right = r-l
                _min += (val*right*left)
            inc.append((r,nums[r])) 
            # print("inc", inc)
            # print(_min)


        for r in range(len(dec)):
            l, val = dec[r]
            left = l - dec[r-1][0] if r > 0 else l+1
            right = len(nums)-l
            _max += (val*right*left)
        for r in range(len(inc)):
            l, val = inc[r]
            left = l - inc[r-1][0] if r > 0 else l+1
            right = len(nums)-l
            _min += (val*right*left)
        return _max - _min
        
    