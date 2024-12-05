import os


def check_x(r, c, grid):
    xmas = [
        grid[r - 1][c + 1],
        grid[r + 1][c - 1],
        grid[r - 1][c - 1],
        grid[r + 1][c + 1],
    ]

    order = xmas[0] != xmas[1] and xmas[2] != xmas[3]
    count = xmas.count("M") == 2 and xmas.count("S") == 2

    return 1 if order and count else 0


def main():
    input = []
    count = 0

    filename = "test.txt" if os.getenv("TEST") == "1" else "input.txt"
    with open(filename, "r") as file:
        for line in file:
            input.append(list(line.strip()))

    for i in range(1, len(input) - 1):
        for j in range(1, len(input[0]) - 1):
            if input[i][j] == "A":
                count += check_x(i, j, input)

    print(count)


if __name__ == "__main__":
    main()
