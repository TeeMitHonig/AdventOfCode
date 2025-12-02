def is_invalid_id(n: int) -> bool:
    s = str(n)
    L = len(s)

    for k in range(1, L // 2 + 1):
        if L % k != 0:
            continue
        repeat = L // k
        if repeat >= 2:
            block = s[:k]
            if block * repeat == s:
                return True
    return False


def sum_invalid_ids(raw_input: str) -> int:
    ranges = raw_input.strip().split(",")
    total = 0

    for r in ranges:
        if not r:
            continue
        start, end = map(int, r.split("-"))
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n

    return total


if __name__ == "__main__":
    with open("./day2-input") as f:
        raw = f.read().strip()
    print(sum_invalid_ids(raw))
