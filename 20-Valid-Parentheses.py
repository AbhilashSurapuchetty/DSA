class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []

        for c in s:
            if c in '({[' :
                stk.append(c)
            else :
                if not stk or (c == ')' and stk[-1] != '(') or (c == ']' and stk[-1] != '[') or (c == '}' and stk[-1] != '{') :
                    return False
                stk.pop()
        if (stk == []) :
            return True
        else :
            return False
            
            
            

        


        