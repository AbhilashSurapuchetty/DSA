class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        i = 0
        while (i < k) :
            c = 0
            res = False
            v = 0
            for j in range(0,len(gifts)) :
                if (c < gifts[j]) :
                    c = gifts[j]
                    res = True
                else :
                    res = False
                if (res) :
                    v = j
            gifts[v] = int(sqrt(gifts[v]))
            i = i + 1
        return sum(gifts)
                
        