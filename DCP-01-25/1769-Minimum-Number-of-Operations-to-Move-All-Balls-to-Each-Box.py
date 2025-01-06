class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        list1 = []
        result = []
        v = len(boxes)
        for i in range(0,v) :
            if (boxes[i] == '1') :
                list1.append(i)
        
        for i in range(0,v) :
            count = 0
            for j in list1 :
                count = count + abs(i-j)
            result.append(count)
        
        return result
        