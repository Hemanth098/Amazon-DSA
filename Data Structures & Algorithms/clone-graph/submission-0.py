"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned_graph = {}

        def dfs(curr_node):
            if curr_node in cloned_graph:
                return cloned_graph[curr_node]
            clone = Node(curr_node.val)
            cloned_graph[curr_node] = clone

            for neighbors in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbors))
            return clone
        return dfs(node)
        