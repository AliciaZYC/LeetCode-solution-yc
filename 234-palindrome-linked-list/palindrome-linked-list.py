# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_vals = []
        # while head:
        #     list_vals.append(head.val)
        #     head = head.next
        # left,right = 0, len(list_vals)-1
        # while left < right and list_vals[left]==list_vals[right]:
        #     left+=1
        #     right-=1
        # return left>=right
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        while curr and curr.val == stack.pop():
            curr = curr.next
        return curr is None