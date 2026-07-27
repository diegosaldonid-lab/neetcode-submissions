class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        islands = 0

        r = len(grid)
        c = len(grid[0])

        def dfs(i,j):
            if r <= i or i < 0 or c <= j or j <0 or (i,j) in visited or grid[i][j] == '0':
                return
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

            return


        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and (i,j) not in visited :
                    islands +=1
                    dfs(i,j)

        return islands 
        