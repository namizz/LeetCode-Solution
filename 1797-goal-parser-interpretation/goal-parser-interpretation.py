class Solution:
    def interpret(self, command: str) -> str:
        o = ['(',')']
        al = ['(','a','l',')']
        store = []
        i = 0
        while i < len(command):
            if command[i] == '(':
                j = i
                while command[i] != ')':
                    i += 1
                
                if i-j > 2:
                    store.append('al')
                else:
                    store.append('o')
            else:
                store.append(command[i])
            i += 1
        return ''.join(store)
                



        