# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. First Reverse the Link 
# 2. Then merge the links 
class Solution:
    def find_middle(self, head: Optional[ListNode]) -> None:
        """
        Returns the index of the ListNode
        """
        # Fast and Slow Pointers
        slow , fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # fast reached the end
        second = slow.next
        slow.next = None
        return second
    
    def reverse_second_half(self, LL: Optional[ListNode]) -> None:
        """
        reverse a linkedlist
        """
        # [ 2, 3, 4]
        curr, prev = LL, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
            
    def merge_two_half(self, first: Optional[ListNode], second: [ListNode]) -> None:
        """
        Merge the Two 
        """
        while second:
                    n1, n2 = first.next, second.next
                    first.next = second
                    second.next = n1
                    first, second = n1, n2

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        second = self.find_middle(head)
        reversed_second = self.reverse_second_half(second)
        self.merge_two_half(head, reversed_second)


        
        