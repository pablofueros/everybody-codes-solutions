def part_1(data: str) -> str:
    dnas = []
    for line in data:
        _, dna = line.split(",")
        dnas.append(dna)
    # search for the child
    n = len(dnas[0])
    for i in range(n):
        chars = []
        for dna in dnas:
            chars.append(dna[i])
        if len(set(chars)) == 1:
            continue

    return ""


def part_2(data: str) -> str:
    return ""


def part_3(data: str) -> str:
    return ""


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
