class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        l = []
        for i in range(1,n+1) :
            if (n % i == 0) :
                l.append(i)
            if (len(l) >= k) :
                break
        if (len(l) < k) :
            return -1
        else :
            return l[k-1]
        