def is_valid(i, j, maze, visited, n):
    if i < 0 or j < 0 or i >= n or j >= n:
        return False
    if maze[i][j] == 0:
        return False
    if visited[i][j]:
        return False
    return True


def rat_maze(maze, i, j, visited, path, paths, n):

    if i == n - 1 and j == n - 1:
        paths.append(path)
        return

    visited[i][j] = True

    if is_valid(i + 1, j, maze, visited, n):
        rat_maze(maze, i + 1, j, visited, path + "D", paths, n)

    if is_valid(i, j + 1, maze, visited, n):
        rat_maze(maze, i, j + 1, visited, path + "R", paths, n)

    if is_valid(i - 1, j, maze, visited, n):
        rat_maze(maze, i - 1, j, visited, path + "U", paths, n)

    if is_valid(i, j - 1, maze, visited, n):
        rat_maze(maze, i, j - 1, visited, path + "L", paths, n)

    visited[i][j] = False

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

n = len(maze)
visited = [[False]*n for _ in range(n)]
paths = []

if maze[0][0] == 1:
    rat_maze(maze, 0, 0, visited, "", paths, n)

print(paths)
