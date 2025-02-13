class Solution:
    def findSumDigits(self,number : int) -> int :
        x = str(number) 
        res = 0
        for i in x :
            res = res + int(i)
        return res

    def maximumSum(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums :
            v = self.findSumDigits(i)
            if v in hash_map :
                hash_map[v].append(i)
            else :
                hash_map[v] = [i]
        result = -1
        for i in hash_map :
            if (len(hash_map[i]) > 1) :
                hash_map[i].sort(reverse = True)
                result = max(result,hash_map[i][0] + hash_map[i][1])
        return result
        