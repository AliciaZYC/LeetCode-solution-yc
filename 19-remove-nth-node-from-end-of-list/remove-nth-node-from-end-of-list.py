# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 双指针技巧：fast 先走 n 步，使 slow 与 fast 保持 n 个节点的距离
        slow, fast = head, head
        
        # 步骤1：fast 指针先前进 n 步
        for _ in range(n):
            fast = fast.next
        
        # 步骤2：边界处理 - 若 fast 已为 None，说明要删除的是头节点（n = 链表长度）
        # 例如：[1,2,3], n=3 → fast 走3步后为 None → 直接返回 head.next (即 2)
        if not fast:
            return head.next
        
        # 步骤3：双指针同步后移，直到 fast 到达最后一个节点（fast.next 为 None）
        # 此时 slow 指向「倒数第 n+1 个节点」（即待删除节点的前驱）
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # 步骤4：跳过倒数第 n 个节点（slow.next 即目标节点）
        slow.next = slow.next.next
        
        return head