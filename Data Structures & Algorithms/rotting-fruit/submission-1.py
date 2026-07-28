class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []

        m = len(grid)
        n = len(grid[0])
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
        
        d = [(1,0),(0,1),(-1,0),(0,-1)]

        ret = 0
        while q:
            level = []
            for x,y in q:
                visited.add((x,y))
                for x_d, y_d in d:
                    nx, ny = x + x_d, y + y_d
                    if nx >= m or nx < 0 or ny >= n or ny < 0 or (nx,ny) in visited or grid[nx][ny] == 0 or grid[nx][ny] == 2:
                        continue
                    grid[nx][ny] = 2
                    level.append((nx,ny))
            q = []
            if len(level):
                q = level.copy()
                ret +=1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return ret

        
        