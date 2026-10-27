# Quest 1: The Battle for the Farmlands

TABLE = {
    "x": 0,
    "A": 0,
    "B": 1,
    "C": 3,
    "D": 5,
}


def part_1(data: str):
    total = 0
    for key, value in TABLE.items():
        total += data.count(key) * value
    return total


def part_2(data: str):
    pairs = [data[i : i + 2] for i in range(0, len(data), 2)]
    total = 0
    for pair in pairs:
        if pair[0] == "x" and pair[1] == "x":
            total += 0
        elif pair[0] == "x":
            total += TABLE[pair[1]]
        elif pair[1] == "x":
            total += TABLE[pair[0]]
        else:
            total += TABLE[pair[0]] + TABLE[pair[1]] + 2
    return total


def part_3(data: str):
    trios = [data[i : i + 3] for i in range(0, len(data), 3)]
    total = 0
    for trio in trios:
        if trio[0] == "x" and trio[1] == "x" and trio[2] == "x":
            total += 0
        elif trio[0] == "x" and trio[1] == "x":
            total += TABLE[trio[2]]
        elif trio[0] == "x" and trio[2] == "x":
            total += TABLE[trio[1]]
        elif trio[1] == "x" and trio[2] == "x":
            total += TABLE[trio[0]]
        elif trio[0] == "x":
            total += TABLE[trio[1]] + TABLE[trio[2]] + 2
        elif trio[1] == "x":
            total += TABLE[trio[0]] + TABLE[trio[2]] + 2
        elif trio[2] == "x":
            total += TABLE[trio[0]] + TABLE[trio[1]] + 2
        else:
            total += TABLE[trio[0]] + TABLE[trio[1]] + TABLE[trio[2]] + 6
    return total


def main():
    pass  # debugging


if __name__ == "__main__":
    main()
