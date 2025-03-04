class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # points = [[]]
        # those points represent a range xs, xe---> where a ballon is streched
        # if arrow is release at x , between xs and xe it brust the the ballon where the range is included
        # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
        # -----------
        #   -------------
        #             ---------------
        #                    ------------------
        # we send arrow on the first ballon, then the rests
        # [xs, xe] what should be the efficient point to brust the first ballon and other if possible
        # x = xe
        # remove all ballon when x is in there range target the next existing ballon
        sort_points = sorted(points, key= lambda x : x[1])
        x = float(inf)
        arrow = 0
        print(sort_points)
        for xs,xe in sort_points:
            if not (xs <= x <= xe):
                arrow += 1
                x = xe
        return arrow

        