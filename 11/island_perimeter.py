from collections import deque

class Solution:
    def islandPerimeter(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.append((i, j))
                    visited.add((i, j))
                    break
            if q:
                break

        perimeter = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                    perimeter += 1
                elif grid[nx][ny] == 0:
                    perimeter += 1
                elif (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny))

        return perimeter

