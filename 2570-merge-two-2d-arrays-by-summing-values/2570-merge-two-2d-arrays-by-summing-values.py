class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        ans = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1][0] > nums2[p2][0]:
                ans.append(nums2[p2])
                p2 += 1
            elif nums1[p1][0] < nums2[p2][0]:
                ans.append(nums1[p1])
                p1 += 1
            else:
                ans.append([nums1[p1][0],nums1[p1][1]+nums2[p2][1]])
                p1 += 1
                p2 += 1
        ans.extend(nums1[p1:])
        ans.extend(nums2[p2:])
        return ans


            
        