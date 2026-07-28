"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        track = {}
        ret = []
        q = deque([node])
        visited = set()
        num = 0

        while q:
            curr = q.popleft()
            if curr.val not in track:
                nnn = Node(curr.val)
                track[curr.val] = nnn
            visited.add(curr.val)
            num +=1
            for n in curr.neighbors:
                if n.val in visited:
                    continue
                if n.val not in track:
                    nn = Node(n.val)
                    track[n.val] = nn 
                track[curr.val].neighbors.append(track[n.val])
                track[n.val].neighbors.append(track[curr.val])
                q.append(n)

        return track[1]
            
        