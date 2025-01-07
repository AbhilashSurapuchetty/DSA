class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        v = len(words)
        s = set()
        for i in range(0,v) :
            for j in range(0,v) :
                if (i == j or len(words[i]) > len(words[j])) :
                    continue
                if (words[j].count(words[i]) > 0) :
                    s.add(words[i])
                    break
        return list(s)
                    
                

        
        