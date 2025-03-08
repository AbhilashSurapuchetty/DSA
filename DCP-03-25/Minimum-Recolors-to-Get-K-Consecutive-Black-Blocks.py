class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        x = len(blocks)
        req = float('inf')
        i = 0
        j = k-1
        cb = 0
        for b in range(i,j+1) :
            if (blocks[b] == 'B') :
                cb = cb + 1
        while (j < x) :  
            if (cb == k) :
                return 0
            else :
                req = min(req,k-cb)
                if (j + 1 == x) :
                    break
                elif(blocks[i] == 'W' and blocks[j+1] == 'B') :
                    cb = cb + 1
                elif (blocks[i] == 'B' and blocks[j+1] == 'W') :
                    cb = cb - 1
            
            i = i + 1
            j = j + 1
        return int(req)