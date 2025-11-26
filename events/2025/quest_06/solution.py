def part_1(data: str) -> str:
    A_knight, a_novice = 0, 0
    for item in data:
        if item == "A":
            A_knight += 1
        elif item == "a":
            a_novice += A_knight
    return str(a_novice)


def part_2(data: str) -> str:
    A_knight, B_knight, C_knight = 0, 0, 0
    a_novice, b_novice, c_novice = 0, 0, 0
    for item in data:
        if item == "A":
            A_knight += 1
        elif item == "B":
            B_knight += 1
        elif item == "C":
            C_knight += 1
        elif item == "a":
            a_novice += A_knight
        elif item == "b":
            b_novice += B_knight
        elif item == "c":
            c_novice += C_knight
    return str(a_novice + b_novice + c_novice)


def part_3(data: str) -> str:
    NEAR = 1000
    REPS = 1000
    total = 0
    items = data * REPS
    n_items = len(items)
    for i in range(n_items):
        target = items[i]
        if target.upper() == target:
            continue
        left = max(0, i - NEAR)
        right = min(n_items, i + NEAR)
        sub = items[left : right + 1]
        num = sub.count(target.upper())
        total += num
    return str(total)


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
