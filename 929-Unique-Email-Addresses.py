class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # namizerfu@gmail.com---> nami : local name @gmail.com: domain
        # for local name if + b/n the name the upcoming letter are ignored
        # for local name if . b/n the name the upcoming letter are ignored
        # we are gonna arrange the strings and append it to hashmap
        # return hashmap length
        # to vaiable domian and local name
        # correct local name--> modify by---> add with domain and add to hashmap
        hashmap = {}
        for e in emails:
            loc, domain = e.split("@")
            correct = []
            for correct_letter in loc:
                if correct_letter == "+":
                    break
                elif correct_letter != ".":
                    correct.append(correct_letter)
            word = "".join(correct) +"@"+ domain
            
            if word not in hashmap:
                hashmap[word] = 0
            hashmap[word] += 1
            correct = []
        return len(hashmap)
            

            



        