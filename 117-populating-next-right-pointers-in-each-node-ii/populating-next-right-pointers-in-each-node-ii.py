"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = deque([root])  # Initialize BFS queue

        while queue:
            prev = None
            level_size = len(queue)

            for _ in range(level_size):  # Process each level
                node = queue.popleft()
                if prev:
                    prev.next = node  # Connect previous node to current
                prev = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Last node in the level points to None
            node.next = None

        return root