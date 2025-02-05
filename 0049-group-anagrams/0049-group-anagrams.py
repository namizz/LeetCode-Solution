class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs = [str]
        # return [[angrams]]
        # make the tuples of string of hashmap and and add the tuple to hashmap and string as array
        hashmap = {}
        ans = []
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if s not in hashmap:
                hashmap[s] = [strs[i]]
            else:
                hashmap[s].append(strs[i])

        for v in hashmap.values():
            ans.append(v)
        return ans
            

        