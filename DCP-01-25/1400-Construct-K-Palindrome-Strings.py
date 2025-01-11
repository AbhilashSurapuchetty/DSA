class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        v = len(s)
        if (v < k) :
            return False
        if (k == v) :
            return True
        
        hash_map = {}

        for i in s :
            if i in hash_map :
                hash_map[i] += 1
                continue
            hash_map[i] = 1
        
        count = 0

        for i in hash_map :
            if (hash_map[i] % 2 != 0) :
                count = count + 1
        if (count > k) :
            return False
        return True
        
        