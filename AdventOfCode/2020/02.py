def part1(data):
    password_configs = parse_data(data)
    valid_passwords = 0
    for rng, ch, password in password_configs:
        count = 0
        for c in password:
            if c == ch:
                count += 1
        if rng[0] <= count <= rng[1]:
            valid_passwords += 1
    return valid_passwords


def part2(data):
    password_configs = parse_data(data)
    valid_passwords = 0
    for rng, ch, password in password_configs:
        count = 0
        for pos in rng:
            if pos - 1 < len(password) and password[pos - 1] == ch:
                count += 1
        if count == 1:
            valid_passwords += 1
    return valid_passwords


def parse_data(data):
    rows = data.split('\n')
    password_configs = []
    for r in rows:
        parts = r.split(' ')
        rng = parts[0].split('-')
        password_configs.append(((int(rng[0]), int(rng[1])), parts[1][0], parts[2]))
    return password_configs
