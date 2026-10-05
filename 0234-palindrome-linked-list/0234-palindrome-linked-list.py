# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        flag = True
        temp = head
        arr = []
        while temp != None:
            arr.append(temp.val)
            temp = temp.next
        print(arr)
        rev = []
        for i in range(len(arr)-1,-1,-1):
            rev.append(arr[i])
        print(rev)
        for i in range(len(arr)):
            if arr[i] != rev[i]:
                return False
                break
        return True