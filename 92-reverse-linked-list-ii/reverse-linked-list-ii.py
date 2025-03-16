# 定义单链表的节点类
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 如果链表为空或 left 和 right 相等，则无需翻转，直接返回原链表
        if not head or left == right:
            return head
        
        # 创建一个虚拟头节点，以便处理头节点的变化
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # 找到 left 位置的前一个节点
        for _ in range(left - 1):
            prev = prev.next
        
        # 使用头插法反转 left 到 right 之间的节点
        current = prev.next
        for _ in range(right - left):
            next_node = current.next  # 记录下一个节点
            # 调整指针顺序，使用头插法逐步反转
            current.next, next_node.next, prev.next = next_node.next, prev.next, next_node
        
        # 返回新的链表头
        return dummy.next
