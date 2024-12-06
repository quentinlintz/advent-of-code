import os
import math


def main():
    sum = 0
    updates = []
    pages = []
    input = []

    filename = "test.txt" if os.getenv("TEST") == "1" else "input.txt"
    with open(filename, "r") as file:
        for line in file:
            input.append(line.strip())

    blank = input.index("")
    updates, pages = input[:blank], input[blank + 1 :]

    for page in pages:
        bad = False
        for update in updates:
            first, second = update.split("|")
            if (
                first in page
                and second in page
                and page.index(second) < page.index(first)
            ):
                bad = True
                break
        if not bad:
            page_list = page.split(",")
            sum += int(page_list[math.floor(len(page_list) / 2)])

    print(sum)


if __name__ == "__main__":
    main()
