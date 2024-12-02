def check_level(level):
    is_increasing = True
    for i in range(1, len(level)):
        if i == 1:
            if level[i - 1] > level[i]:
                is_increasing = False
        if abs(level[i - 1] - level[i]) > 3 or abs(level[i - 1] - level[i]) < 1:
            return False
        elif level[i - 1] > level[i] and is_increasing:
            return False
        elif level[i - 1] < level[i] and not is_increasing:
            return False
    return True


def main():
    levels = []

    with open("input.txt", "r") as file:
        for line in file:
            levels.append([int(number) for number in line.split()])

    safe = len(levels)

    for level in levels:
        good = False
        if check_level(level):
            continue
        # Remove each step and check
        for i in range(len(level)):
            new_level = level[:i] + level[i + 1 :]
            print(new_level)
            if check_level(new_level):
                good = True
                break
        if not good:
            safe -= 1

    print(safe)


if __name__ == "__main__":
    main()
