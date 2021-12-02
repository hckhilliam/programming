def part1(data):
    rows = parse_data(data)
    num_increased = 0

    if len(rows) == 1:
        return num_increased

    curr = int(rows[0])
    for i in range(1, len(rows)):
        num = int(rows[i])
        if num > curr:
            num_increased += 1
        curr = num
    return num_increased


def part2(data):
    rows = parse_data(data)
    num_increased = 0

    if len(rows) <= 1:
        return num_increased

    curr_sum = int(rows[0]) + int(rows[1]) + int(rows[2])
    for i in range(3, len(rows)):
        new_sum = curr_sum - int(rows[i - 3]) + int(rows[i])
        if new_sum > curr_sum:
            num_increased += 1
        curr_sum = new_sum
    return num_increased



def parse_data(data):
    rows = data.split('\n')
    return rows
