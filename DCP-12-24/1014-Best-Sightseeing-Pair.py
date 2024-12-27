class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        v = len(values)

        l = [0] * v
        l[0] = values[0]

        score = 0

        for i in range(1,v) :

            right = values[i] - i

            score = max(score,l[i-1] + right)

            left = values[i] + i

            l[i] = max(l[i-1],left)
        
        return score