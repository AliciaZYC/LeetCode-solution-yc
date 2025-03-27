"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.dfs(node,{})
        
    def dfs(self, node, visited):
        if node is None:
            return None

        newNode = Node(node.val)
        visited[node.val] = newNode

        for adjNode in node.neighbors:
            if adjNode.val not in visited:
                newNode.neighbors.append(self.dfs(adjNode, visited))
            else:
                newNode.neighbors.append(visited[adjNode.val])
        return newNode