import heapq

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, target, R, C):
    (sr, sc) = start
    (tr, tc) = target

    open_set = []
    heapq.heappush(open_set, (0 + manhattan(start, target), 0, start))
    came_from = {}
    g_score = {start: 0}

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while open_set:
        _, cost, current = heapq.heappop(open_set)

        if current == target:
            # reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return cost, path

        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                neighbor = (nr, nc)
                temp_g = cost + 1

                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    g_score[neighbor] = temp_g
                    priority = temp_g + manhattan(neighbor, target)
                    heapq.heappush(open_set, (priority, temp_g, neighbor))
                    came_from[neighbor] = current

    return None, None

with open("input.txt", "r") as f:
    R, C = map(int, f.readline().split())

    grid = []
    for _ in range(R):
        grid.append(list(map(int, f.readline().split())))

    sr, sc = map(int, f.readline().split())
    tr, tc = map(int, f.readline().split())

start = (sr, sc)
target = (tr, tc)

cost, path = a_star(grid, start, target, R, C)

if path is None:
    print("Path not found using A*")
else:
    print(f"Path found with cost {cost} using A*")
    print("Shortest Path:", path)
