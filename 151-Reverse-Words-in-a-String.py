class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        v = ''
        x = len(l)-1
        while (x > -1) :
            v = v + l[x]
            if (x == 0) :
                break
            v = v + ' '
            x = x - 1
        return v


        