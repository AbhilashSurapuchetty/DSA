class Solution:
    def partitionString(self, s: str) -> int:
        hash_map = {}
        result = 1
        for i in s :
            if i in hash_map :
                result = result + 1
                hash_map = {}
                hash_map[i] = 1
            else :
                hash_map[i] = 1
        return result