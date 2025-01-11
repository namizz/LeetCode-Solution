class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        #s:string , k:int
        # return true if number palinromes in s(using all characters) > k
        #a,n,b,e,l,e
        # using hashmap we count the number of single chars
        # if they are > k answer is false
        # else true
        # constraint what if len(s) < k?
        if len(s) < k:
            return False
        hashmap = Counter(s)
        count = 0
        for i in hashmap:
            if hashmap[i]%2 == 1:
                count += 1
        if count <= k:
            return True
        return False
