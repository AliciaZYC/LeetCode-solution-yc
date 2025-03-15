"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy ={}
        p = head
        while p:
            if p not in copy:
                copy[p] = Node(p.val)
            p = p.next
        p = head
        while p:
            if p.next:
                copy[p].next = copy[p.next]
            if p.random:
                copy[p].random = copy[p.random]
            p = p.next
        return copy.get(head)