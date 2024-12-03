import os
import re


def main():
    memory = ""
    pattern = r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
    sum = 0
    filename = "test.txt" if os.getenv("TEST") == "1" else "input.txt"
    with open(filename, "r") as file:
        for line in file:
            memory += line

    pairs = re.findall(pattern, memory)
    disabled = False
    for pair in pairs:
        if pair == "do()":
            disabled = False
        elif pair == "don't()":
            disabled = True
        elif not disabled and pair[:3] == "mul":
            numbers = [int(x) for x in re.findall(r"[0-9]+", pair)]
            sum += numbers[0] * numbers[1]

    print(sum)


if __name__ == "__main__":
    main()
