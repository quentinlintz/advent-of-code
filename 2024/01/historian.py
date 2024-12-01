from collections import Counter


def main():
    # PART 1
    sum = 0
    first_col = []
    second_col = []

    with open("input.txt", "r") as file:
        for line in file:
            first, second = line.split()
            first_col.append(int(first))
            second_col.append(int(second))

    first_col.sort()
    second_col.sort()

    for i in range(len(first_col)):
        sum += abs(first_col[i] - second_col[i])

    print(sum)

    # PART 2
    similarity = 0
    counter = Counter(second_col)

    for num in first_col:
        similarity += counter[num] * num

    print(similarity)


if __name__ == "__main__":
    main()
