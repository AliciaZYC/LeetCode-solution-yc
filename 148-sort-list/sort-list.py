# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # nums=[]
        # if not head:
        #     return head
        # while head:
        #     nums.append(head.val)
        #     head=head.next
        # nums=sorted(nums)
        # head0=ListNode(nums[0])
        # curr=head0
        # for val in nums[1:]:
        #     curr.next=ListNode(val)
        #     curr=curr.next
        # return head0
        if not head or not head.next:
            return head
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)
    def merge(self,l1:ListNode,l2:ListNode):
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next

