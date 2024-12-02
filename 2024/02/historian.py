def main():
    levels = []

    with open("input.txt", "r") as file:
        for line in file:
            levels.append([int(number) for number in line.split()])

    safe = len(levels)

    for level in levels:
        is_increasing = True
        for i in range(1, len(level)):
            if i == 1:
                if level[i - 1] > level[i]:
                    is_increasing = False
            if abs(level[i - 1] - level[i]) > 3 or abs(level[i - 1] - level[i]) < 1:
                safe -= 1
                break
            if level[i - 1] > level[i] and is_increasing:
                safe -= 1
                break
            if level[i - 1] < level[i] and not is_increasing:
                safe -= 1
                break

    print(safe)


if __name__ == "__main__":
    main()
