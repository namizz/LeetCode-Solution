class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        #[1,-1,1,1,1]
        #[1,0,1,2,3]
        prefix_sum = []
        vowels = {'a','e','i','o','u'}
        ans = []
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                if len(prefix_sum) <= 0:
                    prefix_sum.append(1)
                else:
                    prefix_sum.append(1+prefix_sum[-1])
            else:
                if len(prefix_sum) <= 0:
                    prefix_sum.append(0)
                else:
                    prefix_sum.append(0+prefix_sum[-1])
                
        for lp, rp in queries:
            if lp == 0:
                num = prefix_sum[rp]
            else:
                num = prefix_sum[rp] - prefix_sum[lp - 1]
            ans.append(num)
        return ans



        