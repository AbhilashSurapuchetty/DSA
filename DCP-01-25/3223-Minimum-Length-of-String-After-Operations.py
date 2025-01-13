class Solution:
    def minimumLength(self, s: str) -> int:
        hash_map = {}
        for i in s :
            if i in hash_map:
                hash_map[i] += 1
                continue
            hash_map[i] = 1
        result = 0
        for i in hash_map :
            if (hash_map[i] > 2 and hash_map[i] % 2 == 0) :
                hash_map[i] = 2
                
            elif (hash_map[i] > 2 and hash_map[i] % 2 != 0) :
                hash_map[i] = 1
                
            result = result + hash_map[i]
        
        return result
            
        