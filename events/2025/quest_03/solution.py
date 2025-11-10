from collections import Counter


def part_1(data: str) -> str:
    nums = map(int, data.split(","))
    nums_uq = list(set(nums))
    return str(sum(nums_uq))


def part_2(data: str) -> str:
    nums = map(int, data.split(","))
    nums_uq = list(set(nums))[:20]
    return str(sum(nums_uq))


def part_3(data: str) -> str:
    nums = map(int, data.split(","))
    counter = Counter(nums)
    _, reps = counter.most_common(1)[0]
    return str(reps)


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
