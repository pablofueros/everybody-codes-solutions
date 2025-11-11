def part_1(data: str) -> str:
    nums = list(map(int, data.splitlines()))
    # a/b * b/c * ... * y/z = a/z
    turns_2 = nums[0] / nums[-1]
    turns_1 = 2025
    return str(-int(-turns_1 * turns_2))


def part_2(data: str) -> str:
    nums = list(map(int, data.splitlines()))
    # a/b * b/c * ... * y/z = a/z
    turns_2 = nums[0] / nums[-1]
    turns_1 = 10000000000000
    return str(-int(-turns_1 // turns_2))


def part_3(data: str) -> str:
    lines = data.splitlines()
    prev = int(lines[0])
    result = 1
    for line in lines[1:-1]:
        line = list(map(int, line.split("|")))
        result *= prev / line[0]
        prev = line[1]
    turns = 100
    return str(-int(-turns * result * prev / int(lines[-1])))


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
