class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        v = len(s)
        for i in range(0,len(s)) :
            if (s[i] != '*') :
                stk.append(s[i])
                continue
            else :
                stk.pop()
        if (stk == []) :
            return ''
        else :
            y = ''
            for i in stk :
                y = y + i
            return y
        