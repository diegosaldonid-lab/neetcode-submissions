from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)

        for post, pre in prerequisites:
            adj[post].add(pre)
        
        b = [True]

        
        def dfs(adj, node, visited):
            if node in visited:
                b[0] = False
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(adj, nei, visited)
            visited.remove(node)
            return 
        
        visited = set()
        
        for i in range(numCourses):
            if i not in visited:
                dfs(adj, i, visited)

        return b[0]
        