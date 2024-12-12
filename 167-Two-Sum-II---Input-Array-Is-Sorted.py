class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = []
        i = 0
        j = n - 1
        while (i < j) :
            if (numbers[i] + numbers[j] == target) :
                l.append(i+1)
                l.append(j+1)
                break
            elif (numbers[i] + numbers[j] < target) :
                i = i + 1
            else :
                j = j - 1
        return l
        