def is_invalid_id(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]


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
