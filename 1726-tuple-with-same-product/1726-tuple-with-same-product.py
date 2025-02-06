class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # nums = []
        # return number of tuples
        # how do I know if the tuple (a,b,c,d) is a*b = c*d
        # 4 arrangments when I get one answer disinict answer
        # iterate through all possible set and store their product as key and set as value
        hashmap = defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                ans += (hashmap[nums[i]*nums[j]])*8
                hashmap[nums[i]*nums[j]] += 1

        return ans


        