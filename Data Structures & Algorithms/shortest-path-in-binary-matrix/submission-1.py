from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        visited = set()
        m = len(grid)
        n = len(grid[0])

        ret = float('inf')

        q = deque([(0,0,1)])
        d = [(0,1),(1,0),(0,-1),(-1,0),(1,-1),(-1,-1),(1,1),(-1,1)]
        while q:
            x,y,p = q.popleft()
            visited.add((x,y))
            for x_d,y_d in d:
                if x + x_d >= m or x <0 or y + y_d >=n or y <0 or (x + x_d,y + y_d) in visited or grid[x + x_d][y + y_d] == 1:
                    continue
                if x + x_d == m -1 and y + y_d == n-1:
                    ret = min(ret,p+1)
                q.append((x + x_d,y + y_d,p+1))


        return ret if ret != float('inf') else -1