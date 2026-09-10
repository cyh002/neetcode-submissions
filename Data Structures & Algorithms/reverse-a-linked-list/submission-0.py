# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            # save the curr.next
            nxt = curr.next
            # update the pointer to swap position to the previous
            curr.next = prev
            # shift the pointers forward
            prev = curr
            curr = nxt
        return prev

