class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n, group = len(nums), 0
        pairs = sorted([[nums[i], i] for i in range(n)], key=lambda x: x[0])
        map = [0] * n
        sets = [[n - 1, n - 1]]
        for i in range(n - 2, -1, -1):
            if pairs[i + 1][0] - pairs[i][0] <= limit:
                sets[-1][0] = i
                map[pairs[i][1]] = group
            else:
                sets.append([i, i])
                group += 1
                map[pairs[i][1]] = group
        for i in range(n):
            key = map[i]
            nums[i] = pairs[sets[key][0]][0]
            sets[map[i]][0] += 1
        return nums