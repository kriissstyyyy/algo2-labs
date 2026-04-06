from collections import deque


def solve():
    with open('input-dop.txt') as f:
        raw_content = f.read().split()

    if not raw_content:
        return

    h, w = int(raw_content[0]), int(raw_content[1])
    pointer = 2

    field = []
    for _ in range(h):
        field.append([int(val) for val in raw_content[pointer:pointer + w]])
        pointer += w

    seen = set()
    vectors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    land_forms = []

    def get_island_shape(start_y, start_x):
        stack = deque([(start_y, start_x)])
        seen.add((start_y, start_x))
        nodes = []

        while stack:
            y, x = stack.popleft()
            nodes.append((y, x))
            for dy, dx in vectors:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and (ny, nx) not in seen:
                    if field[ny][nx] == 1:
                        seen.add((ny, nx))
                        stack.append((ny, nx))

        y_min = min(n[0] for n in nodes)
        x_min = min(n[1] for n in nodes)
        return tuple(sorted((n[0] - y_min, n[1] - x_min) for n in nodes))

    for r in range(h):
        for c in range(w):
            if field[r][c] == 1 and (r, c) not in seen:
                land_forms.append(get_island_shape(r, c))

    results = {}
    for shape in land_forms:
        results[shape] = results.get(shape, 0) + 1

    twins = sum(qty for qty in results.values() if qty > 1)

    print(f"Total islands: {len(land_forms)}")
    print(f"Twin islands: {twins}")


if __name__ == "__main__":
    solve()