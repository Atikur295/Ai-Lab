# IDDFS Maze Path Finder

def is_valid(x, y, grid, visited):
    rows, cols = len(grid), len(grid[0])
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0 and not visited[x][y]


def dfs_limited(x, y, target, grid, depth_limit, visited, path, traversal):
    traversal.append((x, y))
    
    if (x, y) == target:
        path.append((x, y))
        return True

    if depth_limit == 0:
        return False

    visited[x][y] = True

    # Moves: Up, Down, Left, Right
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, grid, visited):
            if dfs_limited(nx, ny, target, grid, depth_limit - 1, visited, path, traversal):
                path.append((x, y))
                return True

    visited[x][y] = False
    return False


def iddfs(start, target, grid, max_depth):
    for depth in range(max_depth + 1):
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        path = []
        traversal = []
        if dfs_limited(start[0], start[1], target, grid, depth, visited, path, traversal):
            path.reverse()
            return True, depth, path, traversal
    return False, max_depth, [], []


# --------------------------
# 📌 CASE #1
# --------------------------
grid1 = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 1]
]
start1 = (0, 0)
target1 = (2, 3)
max_depth1 = 20

found, depth, path, traversal = iddfs(start1, target1, grid1, max_depth1)

print("Case #1 Result:")
if found:
    print(f"Path found at depth {depth} using IDDFS")
    print("Traversal Order:", traversal)
    print("Final Path:", path)
else:
    print(f"Path not found at max depth {depth} using IDDFS")

print("\n" + "-"*40 + "\n")

# --------------------------
# 📌 CASE #2
# --------------------------
grid2 = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]
start2 = (0, 0)
target2 = (2, 2)
max_depth2 = 6

found, depth, path, traversal = iddfs(start2, target2, grid2, max_depth2)

print("Case #2 Result:")
if found:
    print(f"Path found at depth {depth} using IDDFS")
    print("Traversal Order:", traversal)
    print("Final Path:", path)
else:
    print(f"Path not found at max depth {depth} using IDDFS")
