def part_1(data: str) -> str:
    N_NAILS = 32
    nums = list(map(int, data.split(",")))
    count = 0
    for i in range(len(nums) - 1):
        if (nums[i + 1] - nums[i]) % (N_NAILS / 2) == 0:
            count += 1
    return str(count)


def part_2(data: str) -> str:
    N_NAILS = 8
    nums = list(map(int, data.split(",")))
    count = 0


def part_3(data: str) -> str:
    return ""


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
