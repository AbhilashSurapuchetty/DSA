from collections import Counter
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        hash_map1 = {}
        hash_map2 = Counter()

        for ball,color in queries :
            if ball in hash_map1 :
                old = hash_map1[ball]
                hash_map2[old] -= 1
                if (hash_map2[old] == 0) :
                    del hash_map2[old]
            hash_map1[ball] = color
            hash_map2[color] += 1
            res.append(len(hash_map2))
        return res

        
