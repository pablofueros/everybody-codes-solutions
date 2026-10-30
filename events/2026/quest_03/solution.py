def _iso_to_dec(x, y):
    sum = 0
    i = 0
    while len(x) < len(y):
        x = x[-1 - i] + x
        i += 1
    if len(x) > len(y):
        x = x[len(x) - len(y) :]
    for p, (b, n) in enumerate(zip(x, y)):
        sum += int(n) * int(b) ** (len(x) - p - 1)
    return sum


def part_1(data: str) -> str:
    lines = data.splitlines()
    sum = 0
    for row in lines:
        left, y = row.split()
        _, x = left.split("-")
        sum += _iso_to_dec(x, y)
    return str(sum)


def part_2(data: str) -> str:
    lines = data.splitlines()
    sum = 0
    for row in lines:
        left, y = row.split()
        _, x = left.split("-")
        sum += _iso_to_dec(x, y)
    return str(sum)


def part_3(data: str) -> str:
    lines = data.splitlines()
    sum = 0
    for row in lines:
        left, y = row.split()
        _, x = left.split("-")
        val = _iso_to_dec(x, y)
        # brutforced solution
        valid = True
        for n in range(int(y)):
            new_val = _iso_to_dec(x[::], str(n))
            if int(new_val) == val:
                valid = False
                break
        if valid:
            sum += val
    return str(sum)


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
