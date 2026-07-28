class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(x,y,cache):
            if x == m or y == n:
                return 0
            if x == m - 1 and y == n -1:
                return 1
            if cache[x][y] > 0:
                return cache[x][y]

            cache[x][y] = dfs(x + 1, y, cache) + dfs(x, y + 1, cache)
            return cache[x][y]
        
        cache = [[0] * n for i in range(m)]

        return dfs(0,0,cache)
        