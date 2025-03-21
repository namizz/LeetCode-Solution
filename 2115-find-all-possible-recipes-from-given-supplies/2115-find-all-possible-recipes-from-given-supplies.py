class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # recipe: ingriedient
        # supplies = []
        # recipe's ingriedient made by the supplies and re-used
        # we need to make recipe's first that are contained in the ingridient.
        # We add them to supply
        # recipe check if all the ingridient in supply
        # if not we check in recipe list if available(let's say the avaible food A),
        # we check if the food exists in supplies only else in recipe
        # make the recipe that didn't need any recipe first
        hashmap = {}
        r_set = set(recipes)
        r_supplies = set(supplies)
        def recipe_needed(rec, ing):
            needed_rec = []
            av = True
            for i in ing:
                if i in r_supplies:
                    continue
                elif i in r_set:
                    needed_rec.append(i)
                else:
                    av = False
                    break
            if not av:
                if rec in r_set:
                    r_set.remove(rec)
                return 0
            elif not needed_rec:
                r_supplies.add(rec)
                if rec in r_set:
                    r_set.remove(rec)
                return rec
            else:
                hashmap[rec] = needed_rec
                return 0
      
        ans = []    
        for i in range(len(ingredients)):
            available = recipe_needed(recipes[i],ingredients[i])
            if available:
                ans.append(available)
        b = len(hashmap)+1

        while len(hashmap) and len(hashmap) < b:
            deleted = []
            for k,v in hashmap.items():
                available = recipe_needed(k,v)
                if available:
                    deleted.append(k)
                    ans.append(available)
            for k in deleted:
                del hashmap[k]

            b = min(b-1, len(hashmap)+1)
            
        return ans
        # 
        # this level we get how much rec need to make other recipe



        