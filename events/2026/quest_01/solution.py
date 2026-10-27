from math import ceil, sqrt


def part_1(data: str) -> str:
    x = map(int, data.split(","))
    sum = 0
    # Sn := n**2
    for i in x:
        n = ceil(sqrt(i)) ** 2
        sum += n - i
    return str(sum)


def part_2(data: str) -> str:
    x = map(int, data.split(","))
    sum = 0
    # Sn := n**2 - (n-1)**2 = 4(n - 1), n>=3
    for i in x:
        n = 4 * (max(ceil(i / 4 + 1), 3) - 1)
        sum += n - i
    return str(sum)


def part_3(data: str) -> str:
    x = map(int, data.split(","))
    sum = 0
    # Sn := (2n+1)**2 - 1
    for i in x:
        n = (2 * ceil((sqrt(i + 1) - 1) / 2) + 1) ** 2 - 1
        sum += n - i
    return str(sum)


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
