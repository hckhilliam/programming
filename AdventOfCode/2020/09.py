def part1(data):
    rows = [int(i) for i in parse_data(data)]
    v = set(rows[:25])
    i = 25
    while True:
        if not two_sum(rows[i], v):
            return rows[i]
        v.add(rows[i])
        i += 1


def two_sum(n, rows):
    for r in rows:
        diff = n - r
        if diff in rows:
            return True
    return False


def part2(data):
    rows = [int(i) for i in parse_data(data)]
    num = 22406676
    i = 0
    while rows[i] <= num:
        vals = [rows[i]]
        total = rows[i]
        for j in range(i + 1, len(rows)):
            total += rows[j]
            vals.append(rows[j])
            if total == num:
                return min(vals) + max(vals)
            elif total > num:
                i += 1
                break
    return None


def parse_data(data):
    rows = data.split('\n')
    return rows
