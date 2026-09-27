class Solution:
    def isValid(self, s: str) -> bool:
        if  len(s) % 2 != 0:
            return False
        
        ans = []
        bracketsMap = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in bracketsMap:
                if ans and ans[-1] == bracketsMap[c]:
                    ans.pop()
                else:
                    return False
            else:
                ans.append(c)
            
        return True if not ans else False


        