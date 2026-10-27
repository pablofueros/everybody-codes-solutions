def part_1(data: str) -> str:
    lines = data.splitlines()
    names = lines[0].split(",")
    rules: dict[str, list[str]] = {}
    for line in lines[2:]:
        key, item = line.split(" > ")
        rules[key] = item.split(",")
    for name in names:
        for i, letter in enumerate(name[:-1]):
            if name[i + 1] not in rules[letter]:
                break
        else:
            return name
    return ""


def part_2(data: str) -> str:
    lines = data.splitlines()
    names = lines[0].split(",")
    rules: dict[str, list[str]] = {}
    for line in lines[2:]:
        key, item = line.split(" > ")
        rules[key] = item.split(",")
    sum = 0
    for j, name in enumerate(names, start=1):
        for i, letter in enumerate(name[:-1]):
            if name[i + 1] not in rules[letter]:
                break
        else:
            sum += j
    return str(sum)


def part_3(data: str) -> str:
    return ""


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
