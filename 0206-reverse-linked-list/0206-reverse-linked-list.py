# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        reverse = []
        temp = head
        while temp != None:
            reverse.append(temp.val)
            temp = temp.next
        print(reverse)
        temp = head
        for i in range(len(reverse)-1, -1 , -1):
            temp.val = reverse[i] 
            temp = temp.next
        return head