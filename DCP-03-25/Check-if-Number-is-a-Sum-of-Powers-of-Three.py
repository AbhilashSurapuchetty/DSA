class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        s = ''
        i = n
        while (i > 0) :
            s = s + str(i % 3)
            i = i // 3
        for j in s :
            if (j == '2') :
                return False
        return True






        
        