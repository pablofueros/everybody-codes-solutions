from math import ceil, sqrt


def part_1(data: str) -> str:
    x = map(int, data.split(","))
    sum = 0
    for i in x:
        n = ceil(sqrt(i)) ** 2
        sum += n - i
    return str(sum)


def part_2(data: str) -> str:
    x = map(int, data.split(","))
    sum = 0
    # n**2 - (n-1)**2 = 4(n - 1), n>=3
    for i in x:
        new = 3
        n = 4 * (new - 1)
        while i > n:
            new += 1
            n = 4 * (new - 1)
        sum += n - i
    return str(sum)


def part_3(data: str) -> str:
    x = map(int, data.split(","))
    sum = 0
    for i in x:
        new = 3
        n = (new**2) - 1
        while i > n:
            new += 2
            n = (new**2) - 1
        sum += n - i
    return str(sum)


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
