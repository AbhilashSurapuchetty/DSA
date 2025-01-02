# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = self.get_length(head)
        index = 0
        itr = head
        while (itr) :
            if (index == length // 2) :
                return itr
            itr = itr.next
            index = index + 1

       

    def get_length(self,head: Optional[ListNode]) :
        count = 0
        itr = head
        while (itr) :
            count = count + 1
            itr = itr.next
        return count