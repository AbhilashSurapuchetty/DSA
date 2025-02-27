class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        set1 = set(arr)
        maxCount = 0
        n = len(arr)

        for i in range(n) :
            for j in range(i+1,n) :

                prev = arr[j]
                curr = arr[i] + arr[j]
                count = 2
                while curr in set1 :
                    prev,curr = curr,curr + prev
                    count = count + 1
                    maxCount = max(maxCount,count)
        return maxCount

        