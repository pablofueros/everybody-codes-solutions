def part_1(data: str) -> str:
    lines = data.splitlines()
    sum = 0
    for row in lines:
        left, x = row.split()
        _, y = left.split("-")
        for p, (n, b) in enumerate(zip(x, y)):
            sum += int(n) * int(b) ** (3 - p)
    return str(sum)


def part_2(data: str) -> str:
    lines = data.splitlines()
    sum = 0
    for row in lines:
        left, x = row.split()
        _, y = left.split("-")
        i = 0
        while len(y) < len(x):
            y = y[-1 - i] + y
            i += 1
        if len(y) > len(x):
            y = y[len(y) - len(x) :]
        for p, (n, b) in enumerate(zip(x, y)):
            sum += int(n) * int(b) ** (len(y) - p - 1)
    return str(sum)


def part_3(data: str) -> str:
    lines = data.splitlines()
    sum = 0
    for row in lines:
        left, x = row.split()
        _, y = left.split("-")
        i = 0
        while len(y) < len(x):
            y = y[-1 - i] + y
            i += 1
        if len(y) > len(x):
            y = y[len(y) - len(x) :]
        val = 0
        for p, (n, b) in enumerate(zip(x, y)):
            val += int(n) * int(b) ** (len(y) - p - 1)
        # brutforced solution
        valid = True
        for xx in range(int(x)):
            xx = str(xx)
            yy = y[::]
            i = 0
            while len(yy) < len(xx):
                yy = yy[-1 - i] + yy
                i += 1
            if len(yy) > len(xx):
                yy = yy[len(yy) - len(xx) :]
            val_new = 0
            for p, (n, b) in enumerate(zip(xx, yy)):
                val_new += int(n) * int(b) ** (len(yy) - p - 1)
            if int(val_new) == val:
                valid = False
                break
        if valid:
            sum += val
    return str(sum)


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
