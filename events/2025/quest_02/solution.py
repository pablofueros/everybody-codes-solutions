def sumc(a: list[int], b: list[int]) -> list[int]:
    return [a[0] + b[0], a[1] + b[1]]


def mulc(a: list[int], b: list[int]) -> list[int]:
    return [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]]


def divc(a: list[int], b: list[int]) -> list[int]:
    arr = [a[0] / b[0], a[1] / b[1]]
    return [int(arr[0]), int(arr[1])]


def part_1(data: str) -> str:
    _, arr_str = data.split("=")
    arr = list(map(int, arr_str.strip("[]").split(",")))
    ans = [0, 0]
    for _ in range(3):
        ans = mulc(ans, ans)
        ans = divc(ans, [10, 10])
        ans = sumc(ans, arr)
    return str(ans).replace(" ", "")


def compute_points(arr: list[int], step: int) -> list[list[int]]:
    pts = []
    b = arr[1]
    while b <= arr[1] + 1000:
        a = arr[0]
        while a <= arr[0] + 1000:
            pts.append([a, b])
            a += step
        b += step
    return pts


def part_2(data: str) -> str:
    _, arr_str = data.split("=")
    arr = list(map(int, arr_str.strip("[]").split(",")))
    points = compute_points(arr, step=10)
    count = 0
    for pt in points:
        ans = [0, 0]
        for _ in range(100):
            ans = mulc(ans, ans)
            ans = divc(ans, [100000, 100000])
            ans = sumc(ans, pt)
            if abs(ans[0]) > 1000000 or abs(ans[1]) > 1000000:
                break
        else:
            count += 1
    return str(count)


def part_3(data: str) -> str:
    _, arr_str = data.split("=")
    arr = list(map(int, arr_str.strip("[]").split(",")))
    points = compute_points(arr, step=1)
    count = 0
    for pt in points:
        ans = [0, 0]
        for _ in range(100):
            ans = mulc(ans, ans)
            ans = divc(ans, [100000, 100000])
            ans = sumc(ans, pt)
            if abs(ans[0]) > 1000000 or abs(ans[1]) > 1000000:
                break
        else:
            count += 1
    return str(count)


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
