class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s = ''
        l = []
        self.helper(n,s,l)
        if (len(l) < k) :
            return ''
        
        l.sort()
        return l[k-1]
        


    def helper(self,i,s,l) :
        if (len(s) == i) :
            l.append(s)
            return
        
        for x in ['a','b','c'] :
            if (len(s) > 0 and s[-1] == x) :
                continue
            
            self.helper(i,s+x,l)
        
                
