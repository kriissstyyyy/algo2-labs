import sys
from collections import deque


def solve():
    sys.stdin = open('input.txt')

    raw_data = sys.stdin.read().split()
    if not raw_data:
        return

    rows = int(raw_data[0])
    cols = int(raw_data[1])
    idx = 2

    grid = []
    for _ in range(rows):
        line = [int(x) for x in raw_data[idx:idx + cols]]
        grid.append(line)
        idx += cols

    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(r_start, c_start):
        q = deque([(r_start, c_start)])
        visited[r_start][c_start] = True
        while q:
            cr, cc = q.popleft()
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = True
                        q.append((nr, nc))

    islands_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                islands_count += 1

    print(islands_count)


if __name__ == "__main__":
    solve()