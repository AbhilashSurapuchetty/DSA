class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hash_map = {}
        l = []
        for i in range(0,len(A)) :
            if A[i] in hash_map :
                hash_map[A[i]] += 1
            else :
                hash_map[A[i]] = 1
            if B[i] in hash_map :
                hash_map[B[i]] += 1
            else :
                hash_map[B[i]] = 1
            
            count = 0
            for i in hash_map :
                if (hash_map[i] >= 2) :
                    count = count + 1
            l.append(count)
        
        return l
            

        
            