# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_length(self, head) :
        count = 0
        itr = head
        while (itr) :
            count = count + 1
            itr = itr.next
        return count
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev,curr = dummy,head
        while curr and curr.next :
            # save ptrs
            nxtNode = curr.next.next
            second = curr.next

            # reverse this pair
            second.next = curr
            curr.next = nxtNode
            prev.next = second

            prev = curr
            curr = nxtNode
        return dummy.next



        
        



        