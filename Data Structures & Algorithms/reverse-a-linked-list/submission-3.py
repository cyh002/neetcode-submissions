# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head should be at the end
        prev, curr = None, head
        while curr:
            # save current next
            nxt = curr.next 
            # set the next to the previous 
            curr.next = prev
            # shift the curr point to next
            prev = curr
            curr = nxt
            
        return prev
        