class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #binary search to find both the end and start
        #find the target and if the left side of target is same number continue the binary search else return the start point
        # continue the another binary search if there is starting point continue until the right of the target is not same as the target
        lp , rp = 0, len(nums) - 1
        ans = [-1,-1]
        #to find starting point
        while lp <= rp:
            mid = (lp+rp)//2
            if nums[mid] > target:
                rp = mid - 1
            elif nums[mid] < target:
                lp = mid + 1
            elif nums[mid] == target and mid-1 >= 0 and nums[mid-1] == target:
                rp = mid - 1
            else:
                ans[0] = mid
                break
        lp , rp = ans[0], len(nums)-1
        if lp >= 0:
            while lp <= rp:
                mid = (lp+rp)//2
                if nums[mid] > target:
                    rp = mid - 1
                elif nums[mid] < target:
                    lp = mid + 1
                elif nums[mid] == target and mid+1 <= len(nums) - 1 and nums[mid+1] == target:
                    lp = mid + 1
                else:
                    ans[1] = mid
                    break
        return ans

                

        