from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        q = deque([(sr,sc)])
        r = len(image)
        c = len(image[0])
        visited = set()

        while q:
            c_x,c_y = q.popleft()
            visited.add((c_x,c_y))
            temp = image[c_x][c_y]
            image[c_x][c_y] = color
            neighbors = [(x,y) for x,y in [(c_x+1,c_y),(c_x,c_y+1),(c_x-1,c_y),(c_x,c_y-1)]]
            for (x1,y1) in neighbors:
                if r <= x1 or x1 < 0 or c <= y1 or y1 < 0 or (x1,y1) in visited or image[x1][y1] != temp:
                    continue
                q.append(((x1,y1)))


        return image
        