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
        if node == None:
            return None
        graph_map = {}
        
        def dfs(cur):
            for n in cur.neighbors:
                if n.val not in graph_map:
                    m = Node(n.val)
                    graph_map[n.val] = m
                    dfs(n)
                graph_map[cur.val].neighbors.append(graph_map[n.val])
        graph_map[node.val] = Node(node.val)
        dfs(node)
        return graph_map[node.val]