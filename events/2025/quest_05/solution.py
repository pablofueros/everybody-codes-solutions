from dataclasses import dataclass


@dataclass
class SwordLevel:
    left: int
    mid: int
    right: int

    @property
    def complete(self):
        return


def compute_sword(nums: list[int]):
    sword = [{"left": None, "quality": nums[0], "right": None}]
    for num in nums[1:]:
        for i, segment in enumerate(sword):
            if num < segment["quality"] and not segment["left"]:
                segment["left"] = num
                break
            if num > segment["quality"] and not segment["right"]:
                segment["right"] = num
                break
            if i == len(sword) - 1:
                sword.append({"left": None, "quality": num, "right": None})
                break
    return sword


def compute_quality(nums: list[int]):
    sword = compute_sword(nums)
    return "".join(map(str, [segment["quality"] for segment in sword]))


def part_1(data: str) -> str:
    _, nums_str = data.split(":")
    nums = list(map(int, nums_str.split(",")))
    return compute_quality(nums)


def part_2(data: str) -> str:
    lines = data.splitlines()
    qualities = []
    for line in lines:
        _, nums_str = line.split(":")
        nums = list(map(int, nums_str.split(",")))
        qualities.append(compute_quality(nums))
    sorted_quailies = sorted(map(int, qualities))
    return str(sorted_quailies[-1] - sorted_quailies[0])


def part_3(data: str) -> str:
    lines = data.splitlines()
    swords = []
    for line in lines:
        id, nums_str = line.split(":")
        nums = list(map(int, nums_str.split(",")))
        swords.append((id, compute_sword(nums)))
    ids = []
    for id, sword in swords:
        print(id)
    return ""


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
