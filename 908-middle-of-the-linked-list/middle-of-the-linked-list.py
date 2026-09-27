# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        current = head 
        count = 0
        while current:
            count += 1
            current = current.next 
        current = head
        middle = count//2

        for i in range(middle):
            current = current.next
        return current 
            