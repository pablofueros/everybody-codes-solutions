def part_1(data: str) -> str:
    names_str, _, moves_str = data.splitlines()
    names = names_str.split(",")
    moves = moves_str.split(",")
    item = 0
    n = len(names)
    for move in moves:
        if move[0] == "R":
            item = min(item + int(move[1:]), n - 1)
        elif move[0] == "L":
            item = max(item - int(move[1:]), 0)
    return names[item]


def part_2(data: str) -> str:
    names_str, _, moves_str = data.splitlines()
    names = names_str.split(",")
    moves = moves_str.split(",")
    item, n = 0, len(names)
    for move in moves:
        if move[0] == "R":
            item = (item + int(move[1:])) % n
        elif move[0] == "L":
            item = (item - int(move[1:])) % n
        else:
            raise ValueError(f"Unknown move: {move}")
    return names[item]


def part_3(data: str) -> str:
    names_str, _, moves_str = data.splitlines()
    names = names_str.split(",")
    moves = moves_str.split(",")
    n = len(names)
    for move in moves:
        if move[0] == "R":
            item = +int(move[1:]) % n
        elif move[0] == "L":
            item = -int(move[1:]) % n
        else:
            raise ValueError(f"Unknown move: {move}")
        names[0], names[item] = names[item], names[0]
    return names[0]


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
