# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr = head 
        prev = nxt = None
        while curr != None:
            nxt = curr.next # Preserve the next node add, so that we can reach 
            curr.next = prev # Replace the current next with prev node address
            prev = curr # For the next node current will be the prev
            curr = nxt # Move current to the next node to repeat the process
        return prev