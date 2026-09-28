# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        count = 0 
        current = head
        while current:
            count += 1
            current = current.next
        

        if count == n:
            return head.next
        
        current = head

        for _ in range(count - n - 1):
            current = current.next
        
        current.next = current.next.next

        return head 