import os
import math


def main():
    sum = 0
    updates = []
    pages = []
    bad_pages = []
    input = []

    filename = "test.txt" if os.getenv("TEST") == "1" else "input.txt"
    with open(filename, "r") as file:
        for line in file:
            input.append(line.strip())

    blank = input.index("")
    updates, pages = input[:blank], input[blank + 1 :]

    # Find bad ones first
    for page in pages:
        for update in updates:
            first, second = update.split("|")
            if (
                first in page
                and second in page
                and page.index(second) < page.index(first)
            ):
                bad_pages.append(page.split(","))
                break

    # Now fix them
    for page in bad_pages:
        # Do many passes, YOLO
        for update in updates * 8:
            first, second = update.split("|")
            if (
                first in page
                and second in page
                and page.index(second) < page.index(first)
            ):
                page[page.index(first)], page[page.index(second)] = (
                    page[page.index(second)],
                    page[page.index(first)],
                )

    # Now sum the middles
    for page in bad_pages:
        sum += int(page[math.floor(len(page) / 2)])

    print(sum)


if __name__ == "__main__":
    main()
