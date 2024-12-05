import os


directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def dfs(r, c, grid, direction, count):
    if direction == (0, 0):
        for dr, dc in directions:
            if (
                r + dr < 0
                or r + dr >= len(grid)
                or c + dc < 0
                or c + dc >= len(grid[0])
            ):
                continue
            if grid[r][c] == "X" and grid[r + dr][c + dc] == "M":
                dfs(r + dr, c + dc, grid, (dr, dc), count)
    else:
        dr, dc = direction
        if r + dr < 0 or r + dr >= len(grid) or c + dc < 0 or c + dc >= len(grid[0]):
            return
        elif grid[r][c] == "M" and grid[r + dr][c + dc] == "A":
            dfs(r + dr, c + dc, grid, (dr, dc), count)
        elif grid[r][c] == "A" and grid[r + dr][c + dc] == "S":
            count.append((r + dr, c + dc))


def main():
    input = []
    count = []

    filename = "test.txt" if os.getenv("TEST") == "1" else "input.txt"
    with open(filename, "r") as file:
        for line in file:
            input.append(list(line.strip()))

    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "X":
                dfs(i, j, input, (0, 0), count)

    print(len(count))


if __name__ == "__main__":
    main()
