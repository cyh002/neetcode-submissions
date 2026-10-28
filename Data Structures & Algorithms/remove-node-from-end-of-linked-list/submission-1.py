# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 0 [1, 2, 3, 4]
        # N = 2
        
        # Initializing of the L to be the dummy, and R to be the head
        # L = 0
        # R = 1
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # While R is not null, we move left and right down 
        # R = 3
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next
        